from telegram import Update
from telegram.ext import ContextTypes

from keyboards import calendar_keyboard
from calendar_utils import previous_month, next_month


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


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "ignore":
        return

    if data.startswith("date:"):
        _, year, month, day = data.split(":")

        await query.edit_message_text(
            text=f"✅ You selected\n\n📅 {day}/{month}/{year}"
        )

    elif data.startswith("prev:"):
        _, year, month = data.split(":")
        year = int(year)
        month = int(month)

        year, month = previous_month(year, month)

        await query.edit_message_text(
            text="📅 Select a date",
            reply_markup=calendar_keyboard(year, month),
        )

    elif data.startswith("next:"):
        _, year, month = data.split(":")
        year = int(year)
        month = int(month)

        year, month = next_month(year, month)

        await query.edit_message_text(
            text="📅 Select a date",
            reply_markup=calendar_keyboard(year, month),
        )
