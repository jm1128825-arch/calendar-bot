from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from config import BOT_TOKEN
from handlers import start, calendar, button


def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN not found!")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("calendar", calendar))
    app.add_handler(CallbackQueryHandler(button))

    print("✅ Smart Calendar Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
