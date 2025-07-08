import os, yt_dlp, uuid
from .utils import OUTPUT_PATH


def download_tiktok(url: str):
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    video_file_path = os.path.join(OUTPUT_PATH, str(uuid.uuid4()) + ".mp4")
    ydl_opts = {
        "outtmpl": video_file_path,
        "quiet": False,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return video_file_path
