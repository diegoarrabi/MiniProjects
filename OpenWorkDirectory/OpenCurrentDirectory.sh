#!/bin/zsh

TXT_PATH="/Users/diegoibarra/Developer/1_myProjects/MiniProjects/OpenWorkDirectory/WorkDirectory.txt"

WORK_PATH=$(head -n 1 "$TXT_PATH")

applescript_code=$(cat << EOF
    set directory_path to POSIX file "${WORK_PATH}"
    tell application "Finder"
        open directory_path
        activate
    end tell
EOF
)

if [ -d "$WORK_PATH" ];
then
    echo $WORK_PATH
    osascript -e $applescript_code &

else
    "/Users/diegoibarra/Developer/1_myProjects/MiniProjects/OpenWorkDirectory/AppleScript_Notification.py" $my_path
    open -a Finder
fi