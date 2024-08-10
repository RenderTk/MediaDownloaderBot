from django.shortcuts import render
from django.http import HttpResponse
from mediadownloaderbot.utils import (
    output_path,
    encode_to_base64,
)
import uuid, os
import pyktok as pyk
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

pyk.specify_browser("chrome")


# Create your views here.
def hello(request):
    return HttpResponse("Hello, this is a tiktok downloader!")


@api_view(["POST"])
def download_video_at_highest_quality(request):
    url = request.data.get("url", None)
    if url is None:
        return Response(
            "No se ha proporcionado un url en la form data de la peticion",
            status=status.HTTP_400_BAD_REQUEST,
        )
    video_filename = str(uuid.uuid4())
    output_file_path = os.path.join(output_path, video_filename + ".mp4")
    try:
        pyk.save_tiktok_video(url, output_file_path, "firefox")
        return Response(
            encode_to_base64(output_file_path),
            status=status.HTTP_200_OK,
            content_type="text/plain",
        )
    except Exception as e:
        print("Excepcion: ", e)
        return Response(
            "Ocurrio un error al descargar el tik tok. Talvez el video no tiene habilitado descargas.",
            status=status.HTTP_400_BAD_REQUEST,
        )
