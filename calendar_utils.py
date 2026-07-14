import calendar
from datetime import datetime


def get_current_month():
    now = datetime.now()

    year = now.year
    month = now.month

    cal = calendar.monthcalendar(year, month)

    month_name = calendar.month_name[month]

    return year, month, month_name, cal
