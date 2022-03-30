import random
import string
chara = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
passw = ''.join(random.choice(chara) for i in range(10))
print(passw)