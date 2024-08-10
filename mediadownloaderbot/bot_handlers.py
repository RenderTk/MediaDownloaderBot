import aiohttp
import os
from telegram import Update
from telegram.ext import ContextTypes
from utils import decode_from_base64

DOWNLOAD_YT_VIDEO_BASE_URL = "http://127.0.0.1:9000/yt/download_video/"
DOWNLOAD_YT_AUDIO_BASE_URL = "http://127.0.0.1:9000/yt/download_audio/"
DOWNLOAD_IN_REEL_BASE_URL = "http://127.0.0.1:9000/in/download_video/"
DOWNLOAD_TT_BASE_URL = "http://127.0.0.1:9000/tt/download_video/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}


async def send_generic_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE, text: str
):
    if update.effective_chat is not None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def youtube_vido_or_audio_download(
    update: Update, context: ContextTypes.DEFAULT_TYPE, yt_url: str, filetype: str
):
    chat_id = 0
    if update.effective_chat is not None:
        chat_id = update.effective_chat.id
    else:
        await send_generic_message(update, context, "Ha ocurrido un error")
        return

    async with aiohttp.ClientSession() as session:
        url_to_post = ""
        form_data = aiohttp.FormData()
        form_data.add_field("url", yt_url)
        if filetype == "video":
            url_to_post = DOWNLOAD_YT_VIDEO_BASE_URL
        elif filetype == "audio":
            url_to_post = DOWNLOAD_YT_AUDIO_BASE_URL

        async with session.post(
            url_to_post, data=form_data, headers=HEADERS
        ) as response:
            if response.status == 200:
                encoded_path = await response.text()
                file_path = decode_from_base64(encoded_path)
                print(f"Sending file: {file_path}")
                with open(file_path, "rb") as video_file:
                    await context.bot.send_video(chat_id=chat_id, video=video_file)
                os.remove(file_path)
            else:
                error = await response.text()
                await send_generic_message(
                    update, context, f"Ha ocurrido un error: {error}"
                )


async def instagram_reel_download(
    update: Update, context: ContextTypes.DEFAULT_TYPE, in_reel_url: str
):
    chat_id = 0
    if update.effective_chat is not None:
        chat_id = update.effective_chat.id
    else:
        await send_generic_message(update, context, "Ha ocurrido un error")
        return

    async with aiohttp.ClientSession() as session:
        form_data = aiohttp.FormData()
        form_data.add_field("url", in_reel_url)
        async with session.post(
            DOWNLOAD_IN_REEL_BASE_URL, data=form_data, headers=HEADERS
        ) as response:
            if response.status == 200:
                encoded_path = await response.text()
                reel_video_path = decode_from_base64(encoded_path)
                print(f"Sending file: {reel_video_path}")
                with open(reel_video_path, "rb") as video_file:
                    await context.bot.send_video(chat_id=chat_id, video=video_file)
                os.remove(reel_video_path)
            else:
                error = await response.text()
                await send_generic_message(
                    update, context, f"Ha ocurrido un error: {error}"
                )


async def tik_tok_download(
    update: Update, context: ContextTypes.DEFAULT_TYPE, tik_tok_url: str
):
    chat_id = 0
    if update.effective_chat is not None:
        chat_id = update.effective_chat.id
    else:
        await send_generic_message(update, context, "Ha ocurrido un error")
        return

    async with aiohttp.ClientSession() as session:
        form_data = aiohttp.FormData()
        form_data.add_field("url", tik_tok_url)
        async with session.post(
            DOWNLOAD_TT_BASE_URL, data=form_data, headers=HEADERS
        ) as response:
            if response.status == 200:
                encoded_path = await response.text()
                tik_tok_video_path = decode_from_base64(encoded_path)
                print(f"Sending file: {tik_tok_video_path}")
                with open(tik_tok_video_path, "rb") as video_file:
                    await context.bot.send_video(chat_id=chat_id, video=video_file)
                os.remove(tik_tok_video_path)
            else:
                error = await response.text()
                await send_generic_message(
                    update, context, f"Ha ocurrido un error: {error}"
                )
