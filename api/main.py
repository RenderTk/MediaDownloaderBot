import asyncio, os, uvicorn, enum
from downloader.instagram_downloader import download_reel
from downloader.tik_tok_downloader import download_tiktok
from downloader.youtube_downloader import download_youtube_video, download_youtube_audio
from fastapi import FastAPI
from pathlib import Path
from fastapi import Query, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse


app = FastAPI()


class FileType(str, enum.Enum):
    VIDEO = "video"
    AUDIO = "audio"


def cleanup_file(file_path: str):
    """Delete file after serving"""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error cleaning up file {file_path}: {e}")


@app.get("/youtube")
async def youtube(
    background_tasks: BackgroundTasks,
    file_type: FileType = Query(..., description="video or audio"),
    url: str = Query(..., description="Youtube video URL to download"),
) -> FileResponse:
    try:
        # Run the blocking download function in a thread pool
        loop = asyncio.get_event_loop()
        file_path: str = ""
        media_type: str = ""

        if file_type == FileType.VIDEO:
            file_path = await loop.run_in_executor(None, download_youtube_video, url)
            media_type = "video/mp4"

        else:
            file_path = await loop.run_in_executor(None, download_youtube_audio, url)
            media_type = "audio/mp3"

        # Verify file exists
        if not os.path.exists(file_path):
            raise HTTPException(
                status_code=500, detail="Failed to download youtube video."
            )

        # Schedule file cleanup after response is sent
        background_tasks.add_task(cleanup_file, file_path)

        # Return the file
        return FileResponse(
            file_path, media_type=media_type, filename=Path(file_path).name
        )

    except Exception as e:
        print(f"Download error: {e}")


@app.get("/instagram")
async def instagram(
    background_tasks: BackgroundTasks,
    url: str = Query(..., description="Instagram reel URL to download"),
) -> FileResponse:
    try:
        # Run the blocking download function in a thread pool
        loop = asyncio.get_event_loop()
        file_path = await loop.run_in_executor(None, download_reel, url)

        # Verify file exists
        if not os.path.exists(file_path):
            raise HTTPException(
                status_code=500, detail="Failed to download instagram reel."
            )

        # Schedule file cleanup after response is sent
        background_tasks.add_task(cleanup_file, file_path)

        # Return the file
        return FileResponse(
            file_path, media_type="video/mp4", filename=Path(file_path).name
        )

    except Exception as e:
        print(f"Download error: {e}")


@app.get("/tiktok")
async def youtube(
    background_tasks: BackgroundTasks,
    url: str = Query(..., description="Tiktok URL to download"),
) -> FileResponse:
    try:
        # Run the blocking download function in a thread pool
        loop = asyncio.get_event_loop()
        file_path = await loop.run_in_executor(None, download_tiktok, url)

        # Verify file exists
        if not os.path.exists(file_path):
            raise HTTPException(
                status_code=500, detail="Failed to download tiktok video."
            )

        # Schedule file cleanup after response is sent
        background_tasks.add_task(cleanup_file, file_path)

        # Return the file
        return FileResponse(
            file_path, media_type="video/mp4", filename=Path(file_path).name
        )

    except Exception as e:
        print(f"Download error: {e}")


@app.get("/health_check")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


async def start_api_async():
    config = uvicorn.Config(app, host="0.0.0.0", port=8002, reload=False)
    server = uvicorn.Server(config)
    await server.serve()
