from datetime import date
from dateutil.relativedelta import relativedelta

four_months = date.today() + relativedelta(months=+4)
print(four_months)