from datetime import date, datetime
from dateutil.relativedelta import relativedelta

todaydate=datetime.now()

print(todaydate)

fourmonthsdate=todaydate+relativedelta(month=+4)

print(fourmonthsdate)