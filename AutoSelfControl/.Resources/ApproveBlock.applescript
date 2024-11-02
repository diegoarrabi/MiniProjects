set process_name to "SecurityAgent"

on is_running(process_or_app)
	tell application "System Events" to (name of processes) contains process_or_app
end is_running

if is_running(process_name) then
	tell application "System Events"
		tell process "SecurityAgent"
			set value of text field 1 of window 1 to "Diego Ibarra"
			set value of text field 2 of window 1 to "hahahey"
			click button "Cancel" of window 1
		end tell
	end tell
end if