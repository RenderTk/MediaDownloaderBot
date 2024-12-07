import os, uuid
import re
from TikTokApi import TikTokApi
from .utils import OUTPUT_PATH

TIK_TOK_MS_TOKEN = os.getenv("TIK_TOK_MS_TOKEN")


async def download_async(url, output_path=OUTPUT_PATH):
    """NEED to run py -m playwright install to work"""
    async with TikTokApi() as api:
        await api.create_sessions(
            ms_tokens=[TIK_TOK_MS_TOKEN], num_sessions=1, sleep_after=3
        )
        id = extract_tiktok_video_id(url)
        video = api.video(
            id=id,
            url=url,
        )
        await video.info()
        bytes = await video.bytes()
        video_file_path = os.path.join(output_path, str(uuid.uuid4()) + ".mp4")
        with open(video_file_path, "wb") as file:
            file.write(bytes)
        return video_file_path


def extract_tiktok_video_id(url):
    parts = url.split("/")
    video_id = parts[5].split("?")[0]
    if video_id:
        return video_id

    raise TypeError(
        "URL format not supported. Below is an example of a supported url.\n"
        "https://www.tiktok.com/@therock/video/6829267836783971589"
    )
