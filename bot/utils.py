import os
from telegram import Update
from telegram.ext import ContextTypes

KEY_TO_VIDEO_URL_KEY = 1  # para obtener la URL del video
KEY_TO_YT_DOWNLOAD_OPTIONS_INLINE_KEYBOARD_MESSAGE_OBJ = 2  # usada para interactuar con el mesnaje del keyboard generado en las opciones de descarga de yt
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def send_generic_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE, text: str
):
    if update.effective_chat is not None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
