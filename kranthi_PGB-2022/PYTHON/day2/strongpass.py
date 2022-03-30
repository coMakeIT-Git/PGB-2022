import array
import random
#Generate a random Password according to conditions
max_len=10
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #all digits list
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS #list of all required caharacters
rand_digit = random.choice(DIGITS)#This will generate random digit similARLY ALL
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_upper1 = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol+rand_upper1

for x in range(max_len - 5):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)

temp_pass_list = array.array('u', temp_pass)
random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
        password = password + x
print("Strong password with conditions")
print(password)