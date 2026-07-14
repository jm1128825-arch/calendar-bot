from telegram import Update
from telegram.ext import ContextTypes

from keyboards import calendar_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Welcome to Smart Calendar!\n\n"
        "Use /calendar to open the calendar."
    )


async def calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Select a date",
        reply_markup=calendar_keyboard(),
    )
