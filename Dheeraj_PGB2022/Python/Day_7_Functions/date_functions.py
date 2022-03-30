from datetime import datetime
from dateutil.relativedelta import relativedelta


class DateFunctions:

    def __init__(self):

        self.str_to_datetime("Mar 09 2022 11:20AM")

        self.four_months()

    # Convert string into a datetime object
    def str_to_datetime(self, s):
        date_time = datetime.strptime(s, '%b %d %Y %I:%M%p')
        print(f"Converted Date_Time : {date_time}")
        return date_time

    # Calculate the date 4 months from the current date
    def four_months(self):
        n_date = datetime.today() + relativedelta(months=4)
        n_date = str(n_date).split()[0]
        print(f"Date After 4 months : {n_date}")
        return n_date


run = DateFunctions()
