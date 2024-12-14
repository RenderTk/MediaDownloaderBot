import os
from telegram import Update
from telegram.ext import ContextTypes
from .utils import send_generic_message
from downloader import youtube_downloader


async def youtube_vido_or_audio_download(
    update: Update, context: ContextTypes.DEFAULT_TYPE, yt_url: str, filetype: str
):

    chat_id = 0
    if update.effective_chat is not None:
        chat_id = update.effective_chat.id
    else:
        await send_generic_message(update, context, "Ha ocurrido un error")
        return

    file_path = ""
    if filetype == "video":
        file_path = await youtube_downloader.download_video_async(yt_url)
    elif filetype == "audio":
        file_path = await youtube_downloader.download_audio_async(yt_url)
    print(f"Sending file: {file_path}")
    with open(file_path, "rb") as video_file:
        await context.bot.send_video(
            chat_id=chat_id, video=video_file, caption="Youtube"
        )
    os.remove(file_path)
