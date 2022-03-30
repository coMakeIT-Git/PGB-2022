from dateutil.relativedelta import relativedelta
from datetime import *
from datetime import date, datetime

print(datetime.strptime("Mar 09 2022 11:20AM", '%b %d %Y %I:%M%p'))

current_date=datetime.now()
updateddate = current_date + relativedelta(months=+4)
print(updateddate)