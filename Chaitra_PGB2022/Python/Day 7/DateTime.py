from datetime import datetime
from dateutil.relativedelta import relativedelta

date_string = "Mar 09 2022 11:20AM"
dob = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print("Initial Format: ", date_string)
print("Converted Format: ", dob)

future_date = dob + relativedelta(months=4)
print("\nDate after 4 months: ", future_date)
