import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes


key_to_video_url_key = 1  # para obtener la URL del video
key_to_yt_download_options_inline_keyboard_message_obj = 2  # usada para interactuar con el mesnaje del keyboard generado en las opciones de descarga de yt
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
load_dotenv(".env")
BOT_TOKEN = os.getenv("BOT_TOKEN")

DOWNLOAD_YT_VIDEO_BASE_URL = "http://127.0.0.1:9000/yt/download_video/"
DOWNLOAD_YT_AUDIO_BASE_URL = "http://127.0.0.1:9000/yt/download_audio/"
DOWNLOAD_TT_BASE_URL = "http://127.0.0.1:9000/tt/download_video/"
DOWNLOAD_IN_REEL_BASE_URL = "http://127.0.0.1:9000/in/download_video/"


async def send_generic_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE, text: str
):
    if update.effective_chat is not None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
