import os
from telegram import Update
from telegram.ext import ContextTypes
from .utils import send_generic_message
from downloader import tik_tok_downloader


async def tik_tok_download(
    update: Update, context: ContextTypes.DEFAULT_TYPE, tik_tok_url: str
):
    chat_id = 0
    if update.effective_chat is not None:
        chat_id = update.effective_chat.id
    else:
        await send_generic_message(update, context, "Ha ocurrido un error")
        return

    tik_tok_video_path = await tik_tok_downloader.download_async(tik_tok_url)
    print(f"Sending file: {tik_tok_video_path}")
    with open(tik_tok_video_path, "rb") as video_file:
        await context.bot.send_video(
            chat_id=chat_id, video=video_file, caption="TikTok"
        )
    os.remove(tik_tok_video_path)
