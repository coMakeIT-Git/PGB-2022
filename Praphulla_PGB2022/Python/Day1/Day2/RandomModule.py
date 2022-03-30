import random
def otpGenerator():
    otp=""
    for i in range(4):
        otp+=str(random.randint(1,9))
    print ("\n Your One Time Password is:", otp)
otpGenerator()

import secrets
secretsGenerator = secrets.SystemRandom()
# function for otp generation
otp = secretsGenerator.randrange(100000, 999999)
print("\n Generating 6 digit random OTP", otp)



