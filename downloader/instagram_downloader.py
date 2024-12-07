import os, uuid
import instaloader
from .utils import OUTPUT_PATH

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_SESSION_FILEPATH = os.getenv("INSTAGRAM_SESSION_FILEPATH")

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
        filename=INSTAGRAM_SESSION_FILEPATH,
    )
except Exception as e:
    raise Exception(f"Archivo de sesion de instagram no fue encontrado.: {e}")


async def download_async(url, output_path=OUTPUT_PATH):
    global ins
    try:
        shortcode = url.split("/")[-2]
    except Exception as e:
        print("Excepcion: ", e)
        raise Exception("Error extracting url's shortcode.")
    try:
        post = instaloader.Post.from_shortcode(ins.context, shortcode)
    except Exception as e:
        print("Excepcion: ", e)
        raise Exception("URL de instagram reel invalida.")

    url = post.video_url
    video_filename = str(uuid.uuid4())
    output_file_path = os.path.join(output_path, video_filename)
    ins.download_pic(filename=output_file_path, url=url, mtime=post.date_utc)
    return f"{output_file_path}.mp4"
