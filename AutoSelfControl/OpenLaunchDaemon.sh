#!/bin/bash

# echo "Script executed from: ${PWD}"

# BASEDIR=$(dirname $0)
# echo "Script location: ${BASEDIR}"

DAEMON_PATH="/Users/diegoibarra/Library/LaunchAgents/diegoibarra.AutoSelfControl.plist"
# open -R $DAEMON_PATH
code $DAEMON_PATH
# launchctl unload $DAEMON_PATH
