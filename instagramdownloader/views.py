import os
import uuid
from django.http import HttpResponse, HttpResponseBadRequest
import instaloader
from mediadownloaderbot.utils import (
    output_path,
    decode_from_base64,
)

INSTAGRAM_SESSION_FILE = os.getenv("INSTAGRAM_SESSION_FILEPATH")
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")


# Create your views here.
def hello(request):
    return HttpResponse("Hello, this is a instagram downloader!")


def download_video_at_highest_quality(request, base64_video_url):
    ins = instaloader.Instaloader()
    video_url = decode_from_base64(base64_video_url)
    # Login with sesision file
    try:
        ins.load_session_from_file(
            username=INSTAGRAM_USERNAME,
            filename=INSTAGRAM_SESSION_FILE,
        )
    except Exception:
        return HttpResponseBadRequest(
            "Archivo de sesion de instagram no fue encontrado."
        )
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
