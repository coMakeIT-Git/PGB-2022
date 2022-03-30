import random
import string


class RandomFunction:
    def __init__(self):

        self.gen_otp()

        self.pass_gen()

    # Generate 6 digit random secure OTP
    def gen_otp(self):
        otp = random.randint(100000, 999999)
        print("Generated OTP :", otp)

    # Generate a random Password which meets the following conditions
    # 	a. Password length must be 10 characters long.
    # 	b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
    def pass_gen(self):
        passwd = string.digits + string.punctuation + string.ascii_letters

        password = random.sample(passwd, 6)
        password += random.choice(string.digits)
        password += random.sample(string.ascii_uppercase, 2)
        password += random.choice(string.punctuation)

        random.shuffle(password)
        password = ''.join(password)

        print(f"Generated Password : {password}")
        return password


run = RandomFunction()
