#!/bin/bash

DAEMON_PATH="/Users/diegoibarra/Library/LaunchAgents/diegoibarra.AutoSelfControl.plist"
# open -R $DAEMON_PATH

# launchctl unload "$DAEMON_PATH"
# sleep 2
launchctl load "$DAEMON_PATH"

# for i in {1..5}
# do
#    echo "$i"
#    sleep 1
#    clear
# done

# launchctl unload "$DAEMON_PATH"