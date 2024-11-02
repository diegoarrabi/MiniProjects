on run {}
	set calendar_active to isCalendarActive()
	
	set count_file_path to POSIX file "/Users/diegoibarra/Developer/1_myProjects/MiniProjects/OutlookCalendarUpdate/count"
	
	--Get Previous Count
	set previous_count to paragraph 1 of (read count_file_path)
	
	--Get Current Count	
	tell application "Calendar" to set current_count to (count of events of calendar "Calendar") as string
	
	--Check if they are the same value
	if previous_count is not equal to current_count then
		writeToFile(current_count, count_file_path)
		--tell application "Shortcuts" to run shortcut "Outlook Events Transfer"
		return "Updated: " & getDate()
	end if
	
	if not calendar_active then
		tell application "Calendar" to quit
	end if
end run

on writeToFile(this_data, target_file) -- (string, file path as string)
	try
		set the target_file to the target_file as text
		set the open_target_file to �
			open for access file target_file with write permission
		write this_data to the open_target_file starting at 0
		close access the open_target_file
		return true
	on error
		try
			close access file target_file
		end try
		return false
	end try
end writeToFile

on getDate()
	set {year:y, month:m, day:d} to (current date)
	# pad the day and month if single digit
	set day_str to text -1 thru -2 of ("00" & d)
	set mon_str to text -1 thru -2 of ("00" & (m * 1))
	# make ISO8601 date string without time
	set the_date to (mon_str & "-" & day_str) as string
	return the_date
end getDate

on isCalendarActive()
	set app_name to "Calendar"
	tell application "System Events" to (name of processes) contains app_name
end isCalendarActive