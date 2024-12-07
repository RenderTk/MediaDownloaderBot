import os, uuid
import subprocess
from pytube.exceptions import RegexMatchError
from pytubefix import YouTube
from pytubefix.cli import on_progress
from .utils import OUTPUT_PATH, AUDIO_PATH, VIDEO_PATH


def merge_video_and_audio_from_files(
    video_path: str, audio_path: str, output_path: str
):
    # Comando ffmpeg
    command = [
        "ffmpeg",
        "-i",
        video_path,
        "-i",
        audio_path,
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        output_path,
    ]
    # Ejecuta el comando
    subprocess.run(command, check=True)
    os.remove(video_path)
    os.remove(audio_path)


async def download_video_async(youtube_url, output_path=OUTPUT_PATH):
    try:
        yt = YouTube(youtube_url, on_progress_callback=on_progress)
        best_video_stream = yt.streams.get_highest_resolution()
        best_audio_stream = yt.streams.get_audio_only()
        if best_video_stream is None or best_audio_stream is None:
            raise Exception("No se encontró ningún video con ese link")

        name = uuid.uuid4()
        video_filename = f"{name}.mp4"
        best_video_stream.download(
            output_path=VIDEO_PATH,
            filename=video_filename,
        )
        audio_filename = f"{name}.webm"
        best_audio_stream.download(
            output_path=AUDIO_PATH,
            filename=audio_filename,
        )
        output_file_path = os.path.join(output_path, f"{str(uuid.uuid4())}.mp4")
        merge_video_and_audio_from_files(
            os.path.join(VIDEO_PATH, video_filename),
            os.path.join(AUDIO_PATH, audio_filename),
            output_file_path,
        )
        return output_file_path
    except RegexMatchError as e:
        print("Excepcion: ", e)
        raise Exception("URL de youtube invalida")
    except Exception as e:
        print("Excepcion: ", e)
        raise Exception("Se produjo un error")


async def download_audio_async(youtube_url, output_path=OUTPUT_PATH):
    try:
        yt = YouTube(youtube_url, on_progress_callback=on_progress)
        best_audio_stream = yt.streams.get_audio_only()
        if best_audio_stream is None:
            raise Exception("No se encontró ningún video con ese link")

        name = uuid.uuid4()
        audio_filename = f"{name}.webm"
        best_audio_stream.download(
            output_path=output_path,
            filename=audio_filename,
        )
        output_file_path = os.path.join(output_path, audio_filename)
        return output_file_path
    except RegexMatchError as e:
        print("Excepcion: ", e)
        raise Exception("URL de youtube invalida")
    except Exception as e:
        print("Excepcion: ", e)
        raise Exception("Se produjo un error")
