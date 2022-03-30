import datetime
#Convert string into a datetime object
date_str = 'Mar 09 2022 11:20AM'

date_obj = datetime.datetime.strptime(date_str, '%b %d %Y %I:%M%p')
print("Day-Time:",date_obj)

print("Calculate the date 4 months from the current date ")
import datetime
print((datetime.date.today() + datetime.timedelta(4*365/12)).isoformat())

print("Generate 6 digit random secure OTP")
import random

otp = random.randint(100000, 999999);

print("OTP is", otp);
