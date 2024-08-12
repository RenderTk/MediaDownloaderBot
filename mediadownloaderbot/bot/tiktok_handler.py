import aiohttp
import os
import base64
from telegram import Update
from telegram.ext import ContextTypes
from bot_utils import (
    send_generic_message,
    HEADERS,
    DOWNLOAD_TT_BASE_URL,
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
                tik_tok_video_path = base64.b64decode(encoded_path).decode()
                print(f"Sending file: {tik_tok_video_path}")
                with open(tik_tok_video_path, "rb") as video_file:
                    await context.bot.send_video(chat_id=chat_id, video=video_file)
                os.remove(tik_tok_video_path)
            else:
                error = await response.text()
                await send_generic_message(
                    update, context, f"Ha ocurrido un error: {error}"
                )
