from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from calendar_utils import get_month


def calendar_keyboard(year=None, month=None):
    year, month, month_name, cal = get_month(year, month)

    keyboard = []

    keyboard.append([
        InlineKeyboardButton("Mo", callback_data="ignore"),
        InlineKeyboardButton("Tu", callback_data="ignore"),
        InlineKeyboardButton("We", callback_data="ignore"),
        InlineKeyboardButton("Th", callback_data="ignore"),
        InlineKeyboardButton("Fr", callback_data="ignore"),
        InlineKeyboardButton("Sa", callback_data="ignore"),
        InlineKeyboardButton("Su", callback_data="ignore"),
    ])

    for week in cal:
        row = []

        for day in week:
            if day == 0:
                row.append(
                    InlineKeyboardButton(" ", callback_data="ignore")
                )
            else:
                row.append(
                    InlineKeyboardButton(
                        str(day),
                        callback_data=f"date:{year}:{month}:{day}"
                    )
                )

        keyboard.append(row)

    keyboard.append([
        InlineKeyboardButton(
            "⬅️",
            callback_data=f"prev:{year}:{month}"
        ),
        InlineKeyboardButton(
            month_name,
            callback_data="ignore"
        ),
        InlineKeyboardButton(
            "➡️",
            callback_data=f"next:{year}:{month}"
        ),
    ])

    return InlineKeyboardMarkup(keyboard)
