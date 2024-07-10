import logging
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)
from bot_handlers import youtube_video_download, youtube_audio_download

load_dotenv(".env")
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat is not None and context.user_data is not None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Envia la URL del video de youtube."
        )
        context.user_data["command"] = (
            "youtube"  # Guardar el comando para referencia posterior
        )


async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat is not None and context.user_data is not None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Envia la URL del video de instagram.",
        )
        context.user_data["command"] = (
            "instagram"  # Guardar el comando para referencia posterior
        )


async def tiktok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat is not None and context.user_data is not None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Envia la URL del video de tiktok."
        )
        context.user_data["command"] = (
            "tiktok"  # Guardar el comando para referencia posterior
        )


async def youtube_button_options_click(update, context):
    query = update.callback_query
    url_from_user_input = context.user_data.pop("video_url", None)
    if url_from_user_input is None:
        return

    await query.answer()
    if query.data == "youtube_video":
        await context.bot.send_message(
            update.effective_chat.id, "Enviandote el video..."
        )
        await youtube_video_download(update, context, url_from_user_input)

    elif query.data == "youtube_audio":
        await context.bot.send_message(
            update.effective_chat.id, "Enviandote el audio..."
        )
        await youtube_audio_download(update, context, url_from_user_input)

    else:
        await context.bot.send_message(
            chat_id=query.message.chat_id, text="Opción no válida."
        )
    await context.bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=None,
    )


async def handle_url(update, context):
    if (
        update.effective_chat is None
        or update.message is None
        or context.user_data is None
    ):
        return

    command = context.user_data.pop("command", None)
    if command == "youtube":
        keyboard = [
            [InlineKeyboardButton("Video", callback_data="youtube_video")],
            [InlineKeyboardButton("Audio", callback_data="youtube_audio")],
            [InlineKeyboardButton("Cancelar", callback_data="youtube_cancelar")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.user_data["video_url"] = update.message.text
        await update.message.reply_text(
            "Selecciona el tipo de descarga:", reply_markup=reply_markup
        )
    elif command == "instagram":
        # Logic for downloading Instagram video
        print("instagram")
    elif command == "tiktok":
        # Logic for downloading TikTok video
        print("tiktok")
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="No se reconoce el comando o ha ocurrido un error.",
        )


def run_bot():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    if not BOT_TOKEN:
        raise ValueError("El token del bot no está configurada")
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    youtube_handler = CommandHandler("youtube", youtube)
    instagram_handler = CommandHandler("instagram", instagram)
    tiktok_handler = CommandHandler("tiktok", tiktok)
    application.add_handler(youtube_handler)
    application.add_handler(instagram_handler)
    application.add_handler(tiktok_handler)

    # Manejador para recibir la las interacciones de butones de yt
    application.add_handler(CallbackQueryHandler(youtube_button_options_click))

    # Manejador para recibir la URL después del comando
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_url))
    application.run_polling()


run_bot()
