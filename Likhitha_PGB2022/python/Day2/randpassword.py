import random
import string

source=string.ascii_letters+string.punctuation+string.digits

password=""

password+=random.choice(string.ascii_uppercase)
password+=random.choice(string.digits)
password+=random.choice(string.punctuation)
password+=random.choice(string.ascii_uppercase)

for i in range(6):
    password+=random.choice(source)
    
print("Random password :",password)
