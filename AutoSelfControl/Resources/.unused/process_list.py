from subprocess import run

applescript='tell application "System Events" to set process_list to (name of processes)'
output_raw = run(["osascript", "-e", applescript], capture_output=True, text=True)
raw_output_list = (output_raw.stdout).split(", ")
raw_output_list.sort()

output_list = [ x.strip() for x in raw_output_list ]

for i in output_list:
    print(i)

