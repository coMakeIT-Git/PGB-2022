from random import *
import string
#Generate 6 digit random secure OTP
print("your 6 digit OTP is:")
for x in range(6):
    print(randint(0,6),end="")
print("\n######")
#Generate a random Password
combination = string.ascii_letters + string.digits + string.punctuation
password = ''.join(choice(combination) for i in range(10))
print("your password is:", password)
