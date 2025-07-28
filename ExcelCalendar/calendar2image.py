from datetime import datetime, timedelta
from os import listdir, path
from subprocess import run
from sys import argv

import dataframe_image as dfi
import pandas as pd
from pandas import DataFrame


############################################################################

class TableStyle():
    caution_color = "F86702"
    priority_color = "FB3819"
    head_font = "SF Pro Rounded"
    body_font = "SF Mono"
    header_fontsize = 1.2
    body_fontsize = 1.3
    border_width = 4
    box_color = "353535"
    header_fontcolor = "8E8E8E"
    body_fontcolor = "E0E0E0"
    header_separator_color = "E2E2E2"
    evenrows_color = "424242"
    oddrows_color = "353535"

def clearScreen() -> None:
    print("\x1b[H\x1b[J")

#region MAKETABLE
def makeTable(_from="") -> None:
    # ENTRY POINT FOR LAUNCHDAEMON
    # CALLING THIS SCRIPT FROM LAUNCH DAEMON ALLOWS FOR TABLE TO BE UPDATED
    clearScreen()
    
    
    make_image: bool = True
    
    HEADER = ["COL-01", "COL-02", "COL-03", "C0L-04"]
    
    TASK_COL = HEADER[0]
    DATE_COL = HEADER[1]
    DAYS_COL = HEADER[3]
    DAY_STR_COL = HEADER[2]
    DATE_FORMAT = "%Y-%m-%d"

    dt_day_limit = timedelta(days=day_limit)
    time_now = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    df_todo = pd.read_csv(csv_path, header=None)

    df_todo.rename(columns={0: HEADER[0], 1: HEADER[1]}, inplace=True)
    df_todo[DATE_COL] = pd.to_datetime(df_todo[DATE_COL], format=DATE_FORMAT)
    df_todo[DAY_STR_COL] = ""
    df_todo[DAYS_COL] = df_todo[DATE_COL] - time_now
    df_todo[DATE_COL] = df_todo[DATE_COL].dt.strftime("%m/%d")
    df_soon: DataFrame = df_todo[(df_todo[DAYS_COL] < dt_day_limit) | (df_todo[TASK_COL].str.endswith("!"))]
    if not df_soon.empty:
        for index, row in df_soon.iterrows():
            days_left = row[DAYS_COL].days
            if days_left == 0:
                df_soon.loc[index, TASK_COL] = row[TASK_COL].upper()
                df_soon.loc[index, DAY_STR_COL] = "TODAY!"
            elif days_left == -1:
                df_soon.loc[index, TASK_COL] = row[TASK_COL].upper()
                df_soon.loc[index, DAY_STR_COL] = "YESTERDAY!"
            elif days_left < -1:
                df_soon.loc[index, TASK_COL] = row[TASK_COL].upper()
                df_soon.loc[index, DAY_STR_COL] = f"{days_left} DAYS AGO!"
            elif days_left == 1:
                df_soon.loc[index, DAY_STR_COL] = "Tomorrow"
            elif days_left > 1:
                df_soon.loc[index, DAY_STR_COL] = f"{days_left} Days"
        df_styled = df_soon.style.set_table_styles(styleTable(df_soon, HEADER)).hide()
        try:
            if make_image:
                dfi.export(df_styled, path.join(images_directory, "table.png"), dpi=300)
        except Exception:
            pass

###########################################################################
###########################################################################
###########################################################################


def styleTable(df: pd.DataFrame, headerCol: list) -> list:
    sty = TableStyle()
    border_width = cStyle["border_width"]

    box_color = cStyle["box_color"]

    head_font = cStyle["head_font"]
    header_line_color = cStyle["header_line_color"]
    head_fontsize = cStyle["head_font_size"]
    body_font = cStyle["body_font"]
    body_fontsize = cStyle["body_font_size"]
    head_font_color = cStyle["head_font_color"]
    body_font_color = cStyle["body_font_color"]
    rECo = cStyle["rowCoE"]
    rOCo = cStyle["rowCoO"]

    paddingHead = f"padding-top: {0}em; padding-bottom: {0}em;"  # % (0, 0)
    propsHead = f"font-weight:bold; background-color:#{box_color}; font-family: {head_font}; color: #{head_font_color}; font-size: {head_fontsize}em;"

    paddingBody = f"padding-top: {0.4}em; padding-bottom: {0.4}em;"
    # paddingBody = f"padding-top: {0.3}em; padding-bottom: {0.3}em;"
    # paddingBodyL = f"padding-left: {0.5}em;"
    paddingBodyL = f"padding-left: {0.5}em; padding-top: {0.4}em; padding-bottom: {0.4}em;"
    propsBodyE = f"font-weight:normal; background-color: #{rECo}; font-family: {body_font}; color: #{body_font_color}; font-size: {body_fontsize}em;"
    propsBodyO = f"font-weight:normal; background-color: #{rOCo}; font-family: {body_font}; color: #{body_font_color}; font-size: {body_fontsize}em;"

    bhBottom = f"border-bottom: {border_width - 2}px solid #{header_line_color};"
    bTop = f"border-top: {border_width}px solid #{box_color};"
    bRight = f"border-right: {border_width}px solid #{box_color};"
    bBottom = f"border-bottom: {border_width}px solid #{box_color};"
    bLeft = f"border-left: {border_width}px solid #{box_color};"

    styleList = [
        # COLOR
        {"selector": "th.col_heading", "props": f"{propsHead}; {paddingHead}; {bTop}; {bhBottom};"},
        {"selector": "tbody tr:nth-child(even)", "props": f"{propsBodyE};"},
        {"selector": "tbody tr:nth-child(odd)", "props": f"{propsBodyO};"},
        # ALIGNMENT
        {"selector": "th.col0", "props": f"text-align: left;{bLeft}; {paddingBodyL}; min-width: 450px;"},
        {"selector": "td.col0", "props": f"text-align: left; {paddingBodyL}; {bLeft};"},
        {"selector": "th.col1", "props": "text-align: center;"},
        {"selector": "td.col1", "props": f"text-align: center; {paddingBody}"},
        {"selector": "th.col2", "props": f"text-align: center; {bRight}"},
        {"selector": "td.col2", "props": f"text-align: right; {paddingBody}; {bRight}"},
        {"selector": "td.col3", "props": "display: none"},
        {"selector": "th.col3", "props": "display: none"},
        {"selector": "tbody tr:nth-last-child(1)", "props": f"{paddingBody}"},
        {"selector": "tbody tr:nth-last-child(1)", "props": f"text-align: right; {paddingBody}; {bBottom}"},
    ]

    count = 0
    for index, row in df.iterrows():
        tempToday = {}
        dict_keys = ["selector", "props"]
        tempToday[dict_keys[0]] = ""
        # Priority Tasks
        if "!" in row["TASKS"]:
            tempToday[dict_keys[1]] = "\
                text-decoration: underline solid 0.15em #%s; \
                font-weight: bold; \
                color: #%s;" % (cStyle["priorityCo"], cStyle["priorityCo"])
        elif "!" in row["DAYS"]:
            tempToday[dict_keys[1]] = "font-weight: bold; color: #%s;" % (cStyle["pastCo"])
        else:
            break
        tempToday["selector"] = f"tbody tr:nth-child({count + 1})"
        count += 1
        styleList.append(tempToday)
        del tempToday

    return styleList


###########################################################################


if __name__ == "__main__":
    if len(argv) == 1:
        argv.append("vscode")
    makeTable(argv[1])
