from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.client import get_bot_response

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    bot_response = await get_bot_response(user_message)

    await update.message.reply_text(bot_response)