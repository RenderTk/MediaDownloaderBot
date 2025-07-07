import os, uuid, yt_dlp
from .utils import OUTPUT_PATH

def download(url: str, output_path=OUTPUT_PATH):
    video_file_path = os.path.join(output_path, str(uuid.uuid4()) + ".mp4")
    ydl_opts = {
        "outtmpl": video_file_path,
        "quiet": False,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return video_file_path