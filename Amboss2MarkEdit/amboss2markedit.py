#!/Users/diegoibarra/.config/pyenv/versions/3.13.0/bin/python

import os
import shutil
from subprocess import run
from datetime import datetime


def checkFile(_parent: str, _basename: str):
    count = 1
    filename, fileext = _basename.split('.')
    while True:
        filename, fileext = _basename.split('.')
        filename_mod = f"{filename}_{count:0>3}.{fileext}"
        file_path = os.path.join(_parent, filename_mod)
        if not os.path.isfile(file_path):
            return file_path
        if count == 1000:
            exit()
        count += 1


HOMEDIR = os.path.expanduser("~")
AMBOSS_DIR = os.path.join(HOMEDIR, "Downloads", "amboss")
NOTES_DIR = os.path.join(HOMEDIR, "Local", "notes", "images", "amboss")
IMAGE_PREFIX = "img"
SCREENSHOT_PREFIX = "a_screenshot"
today_date = datetime.today()
TODAY_STR = f"{today_date.month:0>2}{today_date.day:0>2}"

amboss_contents = os.listdir(AMBOSS_DIR)

if len(amboss_contents) > 0:
    amboss_contents = [x for x in amboss_contents if not x.startswith(".")]

    for _item in amboss_contents:
        image_path = None
        if _item.startswith(SCREENSHOT_PREFIX):
            image_path = os.path.join(AMBOSS_DIR, _item)
            _, _item_ext = _item.rsplit(".", 1)
            new_file_name = f"img_{TODAY_STR}.{_item_ext}"
            to_image_path = checkFile(NOTES_DIR, new_file_name)
        elif _item.startswith(IMAGE_PREFIX):
            image_path = os.path.join(AMBOSS_DIR, _item)
            to_image_path = checkFile(NOTES_DIR, _item)
        if image_path:
            print(image_path)
            print(to_image_path)
            shutil.move(image_path, to_image_path)
            
            # COPIES IMAGE OBJECT
            # applescript = f'set the clipboard to (read (POSIX file {to_image_path}) as JPEG picture)'
            # cmd = run(["osascript", "-e", applescript], capture_output=True, text=True)

            markedit_link = f"[_](file://{to_image_path})"
            run(["pbcopy"], input=markedit_link, text=True)
