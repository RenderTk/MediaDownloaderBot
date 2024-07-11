import aiohttp
import os
from telegram import Update
from telegram.ext import ContextTypes
from utils import encode_to_base64

DOWNLOAD_YT_VIDEO_BASE_URL = "http://127.0.0.1:9000/yt/download_video/"
DOWNLOAD_YT_AUDIO_BASE_URL = "http://127.0.0.1:9000/yt/download_audio/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}


async def send_generic_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE, text: str
):
    if update.effective_chat is not None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def youtube_video_download(
    update: Update, context: ContextTypes.DEFAULT_TYPE, yt_video_url: str
):
    chat_id = 0
    if update.effective_chat is not None:
        chat_id = update.effective_chat.id
    else:
        await send_generic_message(update, context, "Ha ocurrido un error")
        return

    encoded_url = f"{DOWNLOAD_YT_VIDEO_BASE_URL}{encode_to_base64(yt_video_url)}"
    async with aiohttp.ClientSession() as session:
        async with session.get(encoded_url, headers=HEADERS) as response:
            if response.status == 200:
                video_path = await response.text()
                print(f"Sending file: {video_path}")
                with open(video_path, "rb") as video_file:
                    await context.bot.send_video(chat_id=chat_id, video=video_file)
                os.remove(video_path)
            else:
                error = await response.text()
                await send_generic_message(
                    update, context, f"Ha ocurrido un error: {error}"
                )


async def youtube_audio_download(
    update: Update, context: ContextTypes.DEFAULT_TYPE, yt_video_url: str
):
    chat_id = 0
    if update.effective_chat is not None:
        chat_id = update.effective_chat.id
    else:
        await send_generic_message(update, context, "Ha ocurrido un error")
        return

    encoded_url = f"{DOWNLOAD_YT_AUDIO_BASE_URL}{encode_to_base64(yt_video_url)}"
    async with aiohttp.ClientSession() as session:
        async with session.get(encoded_url, headers=HEADERS) as response:
            if response.status == 200:
                audio_path = await response.text()
                print(f"Sending file: {audio_path}")
                with open(audio_path, "rb") as audio_file:
                    await context.bot.send_audio(chat_id=chat_id, audio=audio_file)
                os.remove(audio_path)
            else:
                error = await response.text()
                await send_generic_message(
                    update, context, f"Ha ocurrido un error: {error}"
                )
