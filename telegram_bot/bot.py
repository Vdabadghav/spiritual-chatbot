from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram_bot.handlers import handle_message
from telegram_bot.config import settings

def main():
    app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Telegram Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()