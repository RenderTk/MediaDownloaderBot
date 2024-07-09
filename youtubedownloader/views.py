import os
import uuid
import ffmpeg
from django.http import HttpResponse, HttpResponseBadRequest
from pytube import YouTube
from mediadownloaderbot.utils import (
    decode_from_base64,
    merge_video_and_audio_from_files,
    make_safe_filename,
)
from mediadownloaderbot.utils import video_path, audio_path, output_path


# Create your views here.
def hello(request):
    return HttpResponse("Hello, this is a youtube downloader!")


def download_video_at_highest_quality(request, base64_video_url):
    try:
        url = decode_from_base64(base64_video_url)
        yt = YouTube(url)
        best_video_stream = yt.streams.order_by("resolution").last()
        best_audio_stream = yt.streams.get_audio_only()
        if best_video_stream is None or best_audio_stream is None:
            return HttpResponseBadRequest(
                request, "No se encontró ningún video con ese link"
            )
        name = uuid.uuid4()
        video_filename = f"{name}.mp4"
        best_video_stream.download(
            output_path=video_path,
            filename=video_filename,
        )
        audio_filename = f"{name}.webm"
        best_audio_stream.download(
            output_path=audio_path,
            filename=audio_filename,
        )
        merge_video_and_audio_from_files(
            os.path.join(video_path, video_filename),
            os.path.join(audio_path, audio_filename),
            os.path.join(output_path, f"{make_safe_filename(yt.title)}.mp4"),
        )
        return HttpResponse(request, "Descarga completada exitosamente.")
    except ffmpeg.Error as e:
        print(f"FFmpeg error: {e.stderr.decode()}")
        return
    except Exception as e:
        return HttpResponseBadRequest(f"Se produjo un error: {e}")
