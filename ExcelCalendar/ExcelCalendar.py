#!/Users/diegoibarra/.config/pyenv/versions/ExcelCalendar/bin/python

# https://realpython.com/openpyxl-excel-spreadsheets-python/

import sys
from os import path

from subprocess import run

from datetime import date
from datetime import timedelta

from config import *

import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, Border, Side, Font, PatternFill
from openpyxl.cell.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

# ###################################################################


def clearScreen() -> None:
    print("\x1b[H\x1b[J")
# ######################################


def makeWorkbook(file_name: str, file_path: str) -> openpyxl.Workbook:
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = file_name
    workbook.save(file_path)
    return workbook
# ######################################


def openWorkbook(file_path: str) -> None:
    run(['open', file_path])
# ######################################


#  ▗▄▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖▗▄▄▄▖
# ▐▌     █ ▐▌ ▐▌▐▌ ▐▌ █
#  ▝▀▚▖  █ ▐▛▀▜▌▐▛▀▚▖ █
# ▗▄▄▞▘  █ ▐▌ ▐▌▐▌ ▐▌ █
# ###################################################################

clearScreen()
first_str = input("First Month [ex. 'Mar' or 'March']\n: ")
month_first = monthInteger(first_str)
# YEAR = int(input("\nFirst Month Year [ex. '2025']\n: "))
last_str = input("\nLast Month [ex. 'Mar' or 'March']\n: ")
month_last = monthInteger(last_str)
    
month_firstday = date(YEAR, month_first["index"], 1)
if month_last['index'] < month_first['index']:
    YEAR = YEAR+1
month_lastday = date(YEAR, month_last["index"], month_last["days"])

file_name, file_path = makeFileName(first_str, last_str)

firstweek_startdate = getWeekStart(month_firstday)
lastweek_enddate = getWeekEnd(month_lastday)


days_inbetween = (lastweek_enddate - firstweek_startdate)
weeks_in_month = (days_inbetween.days + 1)/7
if weeks_in_month.is_integer():
    weeks_in_month = round(weeks_in_month)
else:
    print("Start Date:", firstweek_startdate)
    print("End Date:  ", lastweek_enddate)
    print("Days:      ", days_inbetween.days+1)
    print("Weeks:     ", weeks_in_month)
    exit(print("weeks in month should be a whole number"))

workbook = makeWorkbook(file_name, file_path)
worksheet = workbook[file_name]
month_iteration = firstweek_startdate.month

# MAKE HEADERS
for day in range(7):
    weekday_cell = worksheet.cell(row=ROW-1, column=(COL+day))
    day_datetime = firstweek_startdate + timedelta(days=day)
    if day == 0:
        day = 7
        worksheet.row_dimensions[ROW-1].height = HEADER_HEIGHT*4/3
    weekday_cell.value = weekday_str[day].upper()
    weekday_cell.alignment = Alignment(horizontal='center', vertical='bottom')
    weekday_cell.font = Font(
        name=FONT_NAME,
        size=16,
        color="000000"
    )


for week in range(weeks_in_month):
    week_firstday = (firstweek_startdate + timedelta(days=(week * 7)))

    for day in range(7):
        WEEK_HEADER = week * 2
        WEEK_BODY = WEEK_HEADER + 1
        if week == 0:
            worksheet.column_dimensions[get_column_letter(COL+day)].width = COL_WIDTH

        if day == 0:
            worksheet.row_dimensions[ROW+WEEK_HEADER].height = HEADER_HEIGHT
            worksheet.row_dimensions[ROW+WEEK_BODY].height = BODY_HEIGHT

        # HEADER
        header_cell = worksheet.cell(row=(ROW+WEEK_HEADER), column=(COL+day))
        day_datetime = week_firstday + timedelta(days=day)
        current_iteration = day_datetime.month
        if not current_iteration == month_iteration:
            month_iteration = current_iteration
        style = monthIteration(month_iteration)

        header_cell.value = day_datetime
        

        header_cell.number_format = 'D'
        header_cell.alignment = Alignment(horizontal='right', vertical='top')
        header_cell.font = Font(
            name=FONT_NAME,
            size=style['header size'],
            color="000000"
        )
        header_cell.fill = PatternFill(
            start_color=style['header'],
            end_color=style['header'],
            fill_type="solid"
        )
        # BODY
        body_cell = worksheet.cell(row=(ROW+WEEK_BODY), column=(COL+day))
        body_cell.alignment = Alignment(
            horizontal='left', 
            vertical='top', 
            wrapText=True,
            indent= 2,
            )
        body_cell.font = Font(
            name=FONT_NAME,
            size=style['body size'],
            color="000000"
        )
        body_cell.fill = PatternFill(
            start_color=style['body'],
            end_color=style['body'],
            fill_type="solid"
        )
        
        h_BOTTOM = style['dash']
        h_TOP = style['thin']
        h_LEFT = style['thin']
        h_RIGHT = style['thin']

        b_BOTTOM = style['thin']
        b_TOP = style['dash']
        b_LEFT = style['thin']
        b_RIGHT = style['thin']

        # FIRST 7 DAYS OF THE MONTH (EXC DAY 1)
        if day_datetime.day in [2, 3, 4, 5, 6, 7]:
            h_TOP = style['thick']
        # FIRST DAY OF MONTH
        if day_datetime.day == 1:
            h_TOP = style['thick']
            h_LEFT = style['thick']
            b_LEFT = style['thick']
        # FIRST DAY OF THE WEEK (SUNDAY)
        if day == 0:
            h_LEFT = style['thick']
            b_LEFT = style['thick']
        # LAST DAY OF THE WEEK (SUNDAY)
        if day == 6:
            h_RIGHT = style['thick']
            b_RIGHT = style['thick']
        if week == 0:
            h_TOP = style['thick']
        if week == (weeks_in_month - 1):
            b_BOTTOM = style['thick']

        header_cell.border = Border(bottom=h_BOTTOM, top=h_TOP, left=h_LEFT, right=h_RIGHT)
        body_cell.border = Border(bottom=b_BOTTOM, top=b_TOP, left=b_LEFT, right=b_RIGHT)
        


workbook.save(file_path)
workbook.close()
openWorkbook(file_path)
sys.exit()
