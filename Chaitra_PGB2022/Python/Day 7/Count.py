s = 0
a = 0
d = 0

str = input("Enter a string: ")
for c in str:
    if(c.isdigit()):
        d += 1
    elif (c.isalpha()):
        a += 1
    elif (c == " "):
        pass
    else:
        s += 1
print("Alphabets: ", a)
print("Digits: ", d)
print("Symbols: ", s)
