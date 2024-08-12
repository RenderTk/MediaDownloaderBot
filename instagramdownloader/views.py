import os
import uuid
import base64
from django.http import HttpResponse, HttpResponseBadRequest
import instaloader
from mediadownloaderbot.utils import (
    output_path,
)
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

load_dotenv(".env")
INSTAGRAM_SESSION_FILE = os.getenv("INSTAGRAM_SESSION_FILEPATH")
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
ins = instaloader.Instaloader(
    download_pictures=False,
    download_video_thumbnails=False,
    download_geotags=False,
    save_metadata=False,
    post_metadata_txt_pattern="",
)
try:
    ins.load_session_from_file(
        username=INSTAGRAM_USERNAME,
        filename=INSTAGRAM_SESSION_FILE,
    )
except Exception as e:
    raise Exception(f"Archivo de sesion de instagram no fue encontrado.: {e}")


# Create your views here.
def hello(request):
    return HttpResponse("Hello, this is a instagram downloader!")


@api_view(["POST"])
def download_video_at_highest_quality(request):
    global ins
    url = request.data.get("url", None)
    if url is None:
        return Response(
            "No se ha proporcionado un url en la form data de la peticion",
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        shortcode = url.split("/")[-2]
    except Exception as e:
        print("Excepcion: ", e)
        return Response("Url invalida.", status=status.HTTP_400_BAD_REQUEST)
    try:
        post = instaloader.Post.from_shortcode(ins.context, shortcode)
    except Exception as e:
        print("Excepcion: ", e)
        return Response(
            f"URL de instagram reel invalida.", status=status.HTTP_400_BAD_REQUEST
        )

    url = post.video_url
    video_filename = str(uuid.uuid4())
    output_file_path = os.path.join(output_path, video_filename)
    ins.download_pic(filename=output_file_path, url=url, mtime=post.date_utc)
    return Response(
        base64.b64encode(bytes(f"{output_file_path}.mp4", "utf-8")),
        status=status.HTTP_200_OK,
    )
