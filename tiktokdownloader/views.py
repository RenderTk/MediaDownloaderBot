from django.shortcuts import render
from django.http import HttpResponse
from mediadownloaderbot.utils import (
    output_path,
    decode_from_base64,
)
import uuid, os
import pyktok as pyk

pyk.specify_browser("chrome")


# Create your views here.
def hello(request):
    return HttpResponse("Hello, this is a tiktok downloader!")


def download_video_at_highest_quality(request, base64_video_url):
    video_url = decode_from_base64(base64_video_url)

    video_filename = str(uuid.uuid4())
    output_file_path = os.path.join(output_path, video_filename + ".mp4")
    pyk.save_tiktok_video(video_url, output_file_path)
    return HttpResponse(output_file_path, content_type="text/plain")
