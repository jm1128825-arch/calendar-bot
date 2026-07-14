import calendar
from datetime import datetime


def get_month(year=None, month=None):
    if year is None or month is None:
        now = datetime.now()
        year = now.year
        month = now.month

    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    return year, month, month_name, cal


def previous_month(year, month):
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    return year, month


def next_month(year, month):
    month += 1
    if month == 13:
        month = 1
        year += 1
    return year, month
