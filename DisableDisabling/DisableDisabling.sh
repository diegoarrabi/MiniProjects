#!/bin/zsh

# osascript -e 'tell app "System Events" to display dialog "Test Window" giving up after (2)'

_return=$(launchctl list | grep diegoibarra.AppBlocker)

if [ "$_return" = "" ]; then
    launchctl load /Users/diegoibarra/Library/LaunchAgents/diegoibarra.AppBlocker.plist
fi


