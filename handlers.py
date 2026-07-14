from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Welcome to Smart Calendar!\n\n"
        "Use /calendar to open your calendar."
    )


async def calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Calendar coming soon..."
    )
