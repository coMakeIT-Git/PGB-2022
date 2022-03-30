string = input("Enter the String: ")
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1

print("Number of Alphabets in this String:  ", alphabets)
print("Number of Digits in this String:  ", digits)
print("Number of Special Characters in this String:  ", special)