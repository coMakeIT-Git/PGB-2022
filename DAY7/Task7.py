import datetime

date_time_str = "Mar 09 2022 11:20AM"
date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')

print('Date-time:', date_time_obj)