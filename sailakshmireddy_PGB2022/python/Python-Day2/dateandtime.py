from datetime import datetime
from dateutil.relativedelta import relativedelta
#Convert string into a datetime object
date_string = "Mar 09 2022 11:20AM"
a= datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print("string into a datetime:",a)
print("##########")

#Calculate the date 4 months from the current date
today_date = datetime.now()
added_months= 4
new_date = today_date + relativedelta(months=+ added_months)
print("new date:",new_date)