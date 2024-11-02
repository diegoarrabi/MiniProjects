TXT_PATH="/Users/diegoibarra/Developer/1_myProjects/MiniProjects/OpenWorkDirectory/WorkDirectory.txt"

my_path=$(head -n 1 "$TXT_PATH")
echo $my_path

if [ -d "$my_path" ];
then
    open -R "$my_path"
else
    "/Users/diegoibarra/Developer/1_myProjects/MiniProjects/OpenWorkDirectory/AppleScript_Notification.py" $my_path
    open -a Finder
fi
