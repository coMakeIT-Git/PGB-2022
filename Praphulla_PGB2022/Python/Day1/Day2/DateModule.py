import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

# Function to convert string to datetime
def convert(date_time):
    format = '%b %d %Y %I:%M%p'
    datetime_string = datetime.datetime.strptime(date_time, format)
    return datetime_string

date_time = 'Mar 09 2022 11:20AM'
print("\n After converting data_string to Date Format:", convert(date_time))

#Calculating date from 4 months from today
four_months = date.today() + relativedelta(months=+4)
print("\n Date 4 months from today is:", four_months)