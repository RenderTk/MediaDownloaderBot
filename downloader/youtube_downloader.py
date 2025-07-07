import os, uuid, yt_dlp
from .utils import OUTPUT_PATH


def download_youtube_video(url: str, output_path=OUTPUT_PATH):
    os.makedirs(output_path, exist_ok=True)
    video_file_path = os.path.join(output_path, str(uuid.uuid4()) + ".mp4")

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Get best quality video+audio
        "outtmpl": video_file_path,
        "quiet": False,
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return video_file_path

def download_youtube_audio(url: str, output_path=OUTPUT_PATH):
    os.makedirs(output_path, exist_ok=True)
    audio_file_path = os.path.join(output_path, str(uuid.uuid4()) + ".mp3")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": audio_file_path,
        "quiet": False,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",  
            "preferredquality": "192",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return audio_file_path



