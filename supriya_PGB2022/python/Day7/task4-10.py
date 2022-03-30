#Find the largest item from a given list without using inbuilt methods
l=[4,76,34,89,2,5]
max=l[0]
for i in range(1,len(l)):
    if(l[i]>max):
        max=l[i]
print(max)
#Convert string into a datetime object
#Input : date_string = "Mar 09 2022 11:20AM"
#output: 2022-03-09 11:20:00
from datetime import datetime
date_time_str = "Mar 09 2022 11:20AM"
date_time_obj = datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
print ("The date is", date_time_obj)
#Calculate the date 4 months from the current date
from datetime import date
from dateutil.relativedelta import relativedelta
four_months = date.today() + relativedelta(months=+4)
print("The date 4 months from current date is",four_months)
#Generate 6 digit random secure OTP
import random
otp = random.randint(100000,999999)
print("OTP",otp)
#Generate a random Password which meets the following conditions
#Password length must be 10 characters long.
#It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
password = random.sample(characters,10)
password+=random.choice(string.digits)
password+=random.choice(string.punctuation)
password+=random.sample(string.ascii_uppercase,2)
password="".join(password)
print("The random password is:",password)

