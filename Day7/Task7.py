#Convert string into a datetime object
	#Input : date_string = "Mar 09 2022 11:20AM"
	#output: 2022-03-09 11:20:00
import datetime

date_time_str = "Mar 09 2022 11:20AM"
date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')

print('Date-time:', date_time_obj)