from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random as rand
import string

#convert string into a datetime object
def strtodate(strdate):
    return datetime.strptime(strdate,"%b %d %Y %I:%M%p")
print("Date is: ",strtodate("Mar 09 2022 11:20AM"))

#Calculating the date 4 months from the current date
def date_func():
    return date.today()+relativedelta(months=+4)
print("Date after 4 months is:", date_func())

# Generate 6 digit random secure OTP
OTP=rand.randint(100000,1000000-1)
print("Secure OTP is",OTP)

#Generating password
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(rand.choice(characters) for i in range(10))
password = rand.sample(characters, 6)
password += rand.sample(string.ascii_uppercase, 2)     # 2 upperkeys
password += rand.choice(string.digits)                 # 1 digit
password += rand.choice(string.punctuation)
password=''.join(password)
print("Random password is:", password)
