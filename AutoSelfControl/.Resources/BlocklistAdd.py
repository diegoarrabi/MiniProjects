#!/usr/bin/python3

from os import path
from subprocess import call


def main():

    url_file_contents = urlList()
    if len(url_file_contents) == 0:
        return
    for item in url_file_contents:
        call(["./AddBlocklist_scpt", item])
    return 


def urlList():
    DESKTOP_PATH = "/Users/diegoibarra/Desktop"
    FILE_NAME = "blocklist_add.txt"

    file_text = path.join(DESKTOP_PATH, FILE_NAME)
    with open(file_text, "r+") as open_textfile:
        raw_text_list = open_textfile.readlines()
        URL_list = [item.strip() for item in raw_text_list]
        # open_textfile.truncate(0)

    return URL_list


if __name__ == '__main__':
    main()
