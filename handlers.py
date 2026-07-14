from keyboards import calendar_keyboard


async def calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Select a date",
        reply_markup=calendar_keyboard(),
    )
