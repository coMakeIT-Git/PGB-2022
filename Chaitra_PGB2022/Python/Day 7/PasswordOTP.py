import string
from random import randint
import random
#OTP
otp = randint(100000,999999)
print("OTP: ", otp)

#Password
password = []
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
symbols = "!@#$%^&*()"
length = 10

password.append(random.choice(string.ascii_letters.upper()))
password.append(random.choice(string.ascii_letters.upper()))
password.append(random.choice(string.digits))
password.append(random.choice(symbols))
for i in range(length-4):
    password.append(random.choice(characters))
random.shuffle(password)
print("Password: ", "".join(password))