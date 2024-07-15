import os
import uuid
from django.http import HttpResponse, HttpResponseBadRequest
import instaloader
from mediadownloaderbot.utils import (
    output_path,
    decode_from_base64,
)
from dotenv import load_dotenv

load_dotenv(".env")
INSTAGRAM_SESSION_FILE = os.getenv("INSTAGRAM_SESSION_FILEPATH")
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
ins = instaloader.Instaloader()
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


def download_video_at_highest_quality(request, base64_video_url):
    video_url = decode_from_base64(base64_video_url)
    try:
        shortcode = video_url.split("/")[-2]
    except Exception as e:
        return HttpResponseBadRequest("Url invalida.")
    try:
        post = instaloader.Post.from_shortcode(ins.context, shortcode)
    except:
        return HttpResponseBadRequest(f"URL de instagram reel invalida.")

    video_url = post.video_url
    video_filename = str(uuid.uuid4())
    output_file_path = os.path.join(output_path, video_filename)
    ins.download_pic(filename=output_file_path, url=video_url, mtime=post.date_utc)
    return HttpResponse(f"{output_file_path}.mp4", content_type="text/plain")
