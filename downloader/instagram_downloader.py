import os, uuid
import instaloader
from .utils import OUTPUT_PATH
from pathlib import Path
from .utils import (
    INSTAGRAM_PASSWORD,
    INSTAGRAM_SESSION_DIR_PATH,
    INSTAGRAM_USERNAME,
    INSTAGRAM_SESSION_FILEPATH,
)


L = instaloader.Instaloader(
    download_pictures=False,
    download_video_thumbnails=False,
    download_geotags=False,
    save_metadata=False,
    post_metadata_txt_pattern="",
)
SESSION_FILE = Path(INSTAGRAM_SESSION_FILEPATH)
if not SESSION_FILE.is_file():
    L.context.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    L.save_session_to_file(
        filename=os.path.join(INSTAGRAM_SESSION_DIR_PATH, INSTAGRAM_USERNAME),
    )
else:
    L.load_session_from_file(
        username=INSTAGRAM_USERNAME,
        filename=INSTAGRAM_SESSION_FILEPATH,
    )


async def download_async(url, output_path=OUTPUT_PATH):
    if L.context.is_logged_in is False:
        L.context.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        L.save_session_to_file(
            filename=os.path.join(INSTAGRAM_SESSION_DIR_PATH, INSTAGRAM_USERNAME),
        )
    try:
        shortcode = url.split("/")[-2]
    except Exception as e:
        print("Excepcion: ", e)
        raise Exception("Error extracting url's shortcode.")
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
    except Exception as e:
        print("Excepcion: ", e)
        raise Exception("URL de instagram reel invalida.")

    url = post.video_url
    video_filename = str(uuid.uuid4())
    output_file_path = os.path.join(output_path, video_filename)
    L.download_pic(filename=output_file_path, url=url, mtime=post.date_utc)
    return f"{output_file_path}.mp4"
