import os, uuid, yt_dlp

OUTPUT_PATH = os.getenv("OUTPUT_PATH")


def download_youtube_video(url: str) -> str:
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    video_file_path = os.path.join(OUTPUT_PATH, str(uuid.uuid4()) + ".mp4")

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": video_file_path,
        "quiet": False,
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return video_file_path


def download_youtube_audio(url: str):
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    audio_file_path = os.path.join(OUTPUT_PATH, str(uuid.uuid4()))

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": audio_file_path,
        "quiet": False,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return audio_file_path + ".mp3"
