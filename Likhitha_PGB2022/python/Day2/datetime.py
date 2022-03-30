from datetime import datetime
# from dateutil import *


# #Convert string into a datetime object

# str = "Mar 09 2022 11:20AM"
# # format = '%b %d %Y %I:%M %p' 

# dateformat = datetime.datetime.strptime(str, '%b %d %Y %I:%M %p')

# print(dateformat)
print(datetime.strptime("Mar 09 2022 11:20AM", '%b %d %Y %I:%M%p'))
