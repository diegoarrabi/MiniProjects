#!/Users/diegoibarra/.config/pyenv/versions/3.13.0/bin/python

from datetime import datetime
from sys import exit
from os import path
from subprocess import call


def main():
    def getTime() -> str:
        my_today = datetime.today()
        tdDay = my_today.day
        tdMonth = my_today.month
        tdHour = my_today.hour
        tdMin = my_today.minute
        timeList = [tdMonth, tdDay, tdHour, tdMin]
        return padNum(timeList)

    def padNum(var: list) -> str:
        for i in range(len(var)):
            timeVar = str(var[i])
            if len(timeVar) < 2:
                timeVar = "0" + timeVar
            var[i] = timeVar
        return comboTime(var)

    def comboTime(var: list) -> str:
        timeStr = ""
        for i in range(len(var)):
            if i == 2:
                timeStr = timeStr + '_' + var[i]
            else:
                timeStr = timeStr + var[i]
        return timeStr

    def openFile(application_file):
        full_path = path.join(application_file)
        my_file = open(full_path, "r+")
        my_file_contents = my_file.readlines()
        my_file.close()
        if len(my_file_contents) == 0:
            exit(print("Text File is empty"))
        for i, text_line in enumerate(my_file_contents):
            my_file_contents[i] = text_line.rstrip()
        return my_file_contents

    # file_name = "ApplicationList.txt"
    # file_contents = openFile(file_name)

    application_list = [
#       "Telegram",
        "Arduino IDE",
#        "Pixelmator Pro",
        "Pixelorama",
        "Swift Playground",
#        "Xcode",
        "Shortcuts",
        "Automator",
        "Messages",
#        "Script Editor",
#        "Visual Studio Code",
        # "Terminal",
    ]

    for title in application_list:
        call(["osascript", "QuitApp.scpt", title, getTime()])


if __name__ == '__main__':
    main()
