import os
from telegram import Update
from telegram.ext import ContextTypes
from .utils import send_generic_message
from downloader import instagram_downloader


async def instagram_reel_download(
    update: Update, context: ContextTypes.DEFAULT_TYPE, in_reel_url: str
):
    chat_id = 0
    if update.effective_chat is not None:
        chat_id = update.effective_chat.id
    else:
        await send_generic_message(update, context, "Ha ocurrido un error")
        return

    reel_video_path = instagram_downloader.download_reel(in_reel_url)
    print(f"Sending file: {reel_video_path}")
    with open(reel_video_path, "rb") as video_file:
        await context.bot.send_video(chat_id=chat_id, video=video_file, caption="Reel")
    os.remove(reel_video_path)
