import random
import string
#input the length of password
length = 10
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
temp = random.sample(all, 10)
password = "".join(temp)
print("\n Generating a Strong password:", password)