#!/usr/bin/env python3

from subprocess import call
from pathlib import Path
import sys
import time

def main(msg):
    full_path = ""
    for i in msg:
        full_path += f' {i}'
    s1 = '-e set dText to "%s"' % (full_path)
    s2 = '-e set dTitle to "Working Directory Path Not Valid"' % (msg)
    s3 = '-e Display Notification dText with title dTitle'
    rtnCode = call(['osascript', s1, s2, s3])

if __name__ == '__main__':
    main(sys.argv[1:])
