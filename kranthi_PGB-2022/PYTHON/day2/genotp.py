# function to generate OTP
import math,random
print("function to generate OTP")
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP
print(generateOTP())