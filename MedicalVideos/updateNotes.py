#!/usr/bin/env python

from os import remove
from os import path as pth
from os import listdir as ls
import subprocess
import time


MAIN_DIR: str = pth.join(pth.expanduser("~"), "Media", "Medical", "BoardsBeyond")
MD_FILE: str = pth.join(MAIN_DIR, "BoardsBeyond.md")

# MAIN_DIR: str = pth.join(pth.expanduser("~"), "Media", "Medical", "BoardsBeyond copy")
# MD_FILE: str = pth.join(MAIN_DIR, "test.md")

SUB_DIRS: list[str] = [pth.join(MAIN_DIR, path)for path in ls(MAIN_DIR) if
                                   not path.startswith(".")
                                   and pth.isdir(pth.join(MAIN_DIR, path))
                                   ]
SUB_DIRS.sort()

remove(MD_FILE)

for topic in SUB_DIRS:
    items = [item for item in ls(topic) if item.endswith('.md')]
    if len(items) > 1:
        print("\x1b[H\x1b[2J")
        exit(print(f"More than one '.md' file in \n {topic}"))
    markdown_file = pth.join(topic, items[0])

    with open(markdown_file, "r") as openTopic:
        markdown_lines = openTopic.readlines()
        markdown_lines.append("\n")

    with open(MD_FILE, "a+") as openMain:
        openMain.writelines(markdown_lines)