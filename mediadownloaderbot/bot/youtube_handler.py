import aiohttp
import os
import base64
from telegram import Update
from telegram.ext import ContextTypes
from bot_utils import (
    send_generic_message,
    HEADERS,
    DOWNLOAD_YT_VIDEO_BASE_URL,
    DOWNLOAD_YT_AUDIO_BASE_URL,
)


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
                file_path = base64.b64decode(encoded_path).decode()
                print(f"Sending file: {file_path}")
                with open(file_path, "rb") as video_file:
                    await context.bot.send_video(chat_id=chat_id, video=video_file)
                os.remove(file_path)
            else:
                error = await response.text()
                await send_generic_message(
                    update, context, f"Ha ocurrido un error: {error}"
                )
