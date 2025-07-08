import logging, os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)
from .utils import (
    KEY_TO_VIDEO_URL_KEY,
    KEY_TO_YT_DOWNLOAD_OPTIONS_INLINE_KEYBOARD_MESSAGE_OBJ,
    BOT_TOKEN,
)
from .youtube_handler import youtube_vido_or_audio_download
from .instagram_handler import instagram_reel_download
from .tiktok_handler import tik_tok_download


async def clean_bot_stuff(context: ContextTypes.DEFAULT_TYPE):
    if context.user_data is None:
        return
    message = context.user_data.pop(
        KEY_TO_YT_DOWNLOAD_OPTIONS_INLINE_KEYBOARD_MESSAGE_OBJ, None
    )
    if message is None:
        return
    if message.reply_markup is not None:
        await context.bot.edit_message_reply_markup(
            chat_id=message.chat_id,
            message_id=message.message_id,
        )


async def handle_url(update, context):
    try:
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
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.user_data[KEY_TO_VIDEO_URL_KEY] = (
                update.message.text
            )  # save video url
            message = await update.message.reply_text(
                "Selecciona el tipo de descarga:", reply_markup=reply_markup
            )
            context.user_data[
                KEY_TO_YT_DOWNLOAD_OPTIONS_INLINE_KEYBOARD_MESSAGE_OBJ
            ] = message

        elif command == "instagram":
            await context.bot.send_message(
                update.effective_chat.id, "Enviandote el reel..."
            )
            await instagram_reel_download(
                update, context, in_reel_url=update.message.text
            )
        elif command == "tiktok":
            await context.bot.send_message(
                update.effective_chat.id, "Enviandote el tik tok..."
            )
            await tik_tok_download(update, context, tik_tok_url=update.message.text)
        else:
            await clean_bot_stuff(context)
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="No se reconoce el comando o ha ocurrido un error.",
            )
    except Exception as e:
        print("Excepcion: ", e)
        await clean_bot_stuff(context)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Ocurrio un error: {e}",
        )


async def youtube_button_options_click(update, context):
    try:
        query = update.callback_query
        url_from_user_input = context.user_data.pop(KEY_TO_VIDEO_URL_KEY, None)
        if url_from_user_input is None:
            return

        await query.answer()
        if query.data == "youtube_video":  # video button
            await clean_bot_stuff(context)
            await context.bot.send_message(
                update.effective_chat.id, "Enviandote el video..."
            )
            await youtube_vido_or_audio_download(
                update, context, url_from_user_input, "video"
            )
        elif query.data == "youtube_audio":  # audio button
            await clean_bot_stuff(context)
            await context.bot.send_message(
                update.effective_chat.id, "Enviandote el audio..."
            )
            await youtube_vido_or_audio_download(
                update, context, url_from_user_input, "audio"
            )
        else:
            await context.bot.send_message(
                chat_id=query.message.chat_id, text="Opción no válida."
            )
        await clean_bot_stuff(context)

    except Exception as e:
        print("Excepcion: ", e)
        await clean_bot_stuff(context)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Ocurrio un error: {e}",
        )


async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await clean_bot_stuff(context)
    if update.effective_chat is not None and context.user_data is not None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Envia la URL del video de youtube."
        )
        context.user_data["command"] = (
            "youtube"  # Guardar el comando para referencia posterior
        )


async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await clean_bot_stuff(context)
    if update.effective_chat is not None and context.user_data is not None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Envia la URL del reel de instagram.",
        )
        context.user_data["command"] = (
            "instagram"  # Guardar el comando para referencia posterior
        )


async def tiktok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await clean_bot_stuff(context)
    if update.effective_chat is not None and context.user_data is not None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Envia la URL del video de tiktok."
        )
        context.user_data["command"] = (
            "tiktok"  # Guardar el comando para referencia posterior
        )


async def start_bot_async():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    if not BOT_TOKEN:
        raise ValueError("El token del bot no está configurado")

    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .read_timeout(360)
        .write_timeout(360)
        .build()
    )

    # Add handlers
    application.add_handler(CommandHandler("youtube", youtube))
    application.add_handler(CommandHandler("instagram", instagram))
    application.add_handler(CommandHandler("tiktok", tiktok))
    application.add_handler(CallbackQueryHandler(youtube_button_options_click))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_url))

    # ✅ This is all you need now (fully async)
    await application.initialize()
    await application.start()
    # Start polling manually
    await application.updater.start_polling()
