from pathlib import Path
from os import path

from datetime import datetime
from datetime import timedelta

from openpyxl.styles import Side


YEAR = 2025
# FONT
FONT_NAME = "SF Pro Text"

# CELL PROPERTIES
ROW = 3
COL = 2
HEADER_HEIGHT = 25
BODY_HEIGHT = 75
COL_WIDTH = 21



month_dict = {
    "january": {"index": 1, "days": 31},
    "february": {"index": 2, "days": 28},
    "march": {"index": 3, "days": 31},
    "april": {"index": 4, "days": 30},
    "may": {"index": 5, "days": 31},
    "june": {"index": 6, "days": 30},
    "july": {"index": 7, "days": 31},
    "august": {"index": 8, "days": 31},
    "september": {"index": 9, "days": 30},
    "october": {"index": 10, "days": 31},
    "november": {"index": 11, "days": 30},
    "december": {"index": 12, "days": 31},
}
month_abbr = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december",
}
weekday_str = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}


def makeFileName(start: str, last: str):
    MONTH_START = month_abbr[start.lower()].capitalize()
    MONTH_LAST = month_abbr[last.lower()].capitalize()
    SHEET_NAME = f"{MONTH_START}-{MONTH_LAST}"
    FILE_BASENAME = f"{SHEET_NAME}.xlsx"
    downloads_directory = path.join(Path.home(), 'Downloads')
    if not path.exists(downloads_directory):
        downloads_directory = Path.home()
    print(f"Creating Calendar from {MONTH_START} to {MONTH_LAST}...")
    FILE_PATH = path.join(downloads_directory, FILE_BASENAME)
    return (SHEET_NAME, FILE_PATH)

def monthIteration(month: int) -> dict:
    month_style = {
        "header": "",
        "body": "",
        "header size": 14,
        "body size": 12,
        "thick": Side(style='medium'),
        "thin": None,
        "dash": None,
    }
    if month % 2 == 1:
        month_style["header"] = "D9D9D9"
        month_style["body"] = "E6E6E6"
        month_style["thin"] = Side(style='thin', color='343434')
        month_style["dash"] = Side(style='dashDotDot', color='343434')

    else:
        month_style["header"] = "F2F2F2"
        month_style["body"] = "FFFFFF"
        month_style["thin"] = Side(style='thin', color='B0B0B0')
        month_style["dash"] = Side(style='dashDotDot', color='B0B0B0')
    return month_style

def monthInteger(month: str) -> dict:
    month = month.lower()
    if YEAR in [2028, 2032, 2036]:
        month_dict["february"]["days"] = 29
    if len(month) == 3:
        month = month_abbr[month]
    return month_dict[month]

def getWeekStart(start_date: datetime) -> datetime:
    weekday_firstday = start_date.isoweekday()
    if weekday_firstday == 7:
        return start_date
    return (start_date - timedelta(weekday_firstday))

def getWeekEnd(end_date: datetime) -> datetime:
    weekday_lastday = end_date.isoweekday()
    if weekday_lastday == 6:
        return end_date
    days = 6 - weekday_lastday
    return (end_date + timedelta(days))
