import os
import uuid
import base64
from django.http import HttpResponse, HttpResponseBadRequest
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from mediadownloaderbot.utils import (
    encode_to_base64,
    merge_video_and_audio_from_files,
    make_safe_filename,
)
from mediadownloaderbot.utils import video_path, audio_path, output_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def hello(request):
    return HttpResponse("Hello, this is a youtube downloader!")


@api_view(["POST"])
def download_video_at_highest_quality(request):
    try:
        url = request.data.get("url", None)
        if url is None:
            return Response(
                "No se ha proporcionado un url en la form data de la peticion",
                status=status.HTTP_400_BAD_REQUEST,
            )
        yt = YouTube(url)
        best_video_stream = yt.streams.order_by("resolution").last()
        best_audio_stream = yt.streams.get_audio_only()
        if best_video_stream is None or best_audio_stream is None:
            return Response(
                request,
                "No se encontró ningún video con ese link",
                status=status.HTTP_400_BAD_REQUEST,
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
        output_file_path = os.path.join(
            output_path, f"{make_safe_filename(yt.title)}.mp4"
        )
        merge_video_and_audio_from_files(
            os.path.join(video_path, video_filename),
            os.path.join(audio_path, audio_filename),
            output_file_path,
        )
        return Response(
            base64.b64encode(bytes(output_file_path, "utf-8")),
            status=status.HTTP_200_OK,
        )
    except RegexMatchError as e:
        print("Excepcion: ", e)
        return Response(
            "URL de youtube invalida",
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as e:
        print("Excepcion: ", e)
        return Response(
            "Se produjo un error",
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def download_audio_of_video_at_highest_quality(request):
    try:
        url = request.data.get("url", None)
        if url is None:
            return Response(
                "No se ha proporcionado un url en la form data de la peticion",
                status=status.HTTP_400_BAD_REQUEST,
            )
        yt = YouTube(url)
        best_audio_stream = yt.streams.get_audio_only()
        if best_audio_stream is None:
            return Response(
                request,
                "No se encontró ningún video con ese link",
                status=status.HTTP_400_BAD_REQUEST,
            )
        name = uuid.uuid4()
        audio_filename = f"{name}.webm"
        best_audio_stream.download(
            output_path=audio_path,
            filename=audio_filename,
        )
        output_file_path = os.path.join(audio_path, audio_filename)
        return Response(encode_to_base64(output_file_path), status=status.HTTP_200_OK)
    except RegexMatchError as e:
        print("Excepcion: ", e)
        return Response(f"URL de youtube invalida", status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("Excepcion: ", e)
        return Response(f"Se produjo un error", status=status.HTTP_400_BAD_REQUEST)
