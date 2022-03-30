from datetime import datetime
from dateutil.relativedelta import relativedelta
import math,random
import string

#n digit random secure OTP
def generate_Otp(n):
	ans=""
	for i in range(n):
		x=math.floor(random.random()*10)
		ans+=str(x)
	return ans
print("Random 6 digit otp ",generate_Otp(6))
#Convert string into a datetime object
datetime_str="Mar 09 2022 11:20AM"
datetime_object = datetime.strptime(datetime_str, '%b %d %Y %I:%M%p')
print(datetime_object)
#calculating the date 4 months from the current date 
four_months = datetime.today() + relativedelta(months=+4)
print("date after 4 months from now: ",four_months)

#Random Password length must be 10 characters long and It must contain at least 2 upper case letters, 1 digit, and 1 special symbol
def password():
	characters = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(characters) for i in range(10))
	password = random.sample(characters, 6)
	password += random.sample(string.ascii_uppercase, 2)     # 2 upperkeys
	password += random.choice(string.digits)                 # 1 digit
	password += random.choice(string.punctuation)
	random.shuffle(password)
	password=''.join(password)
	return password

print("random password ",password())
