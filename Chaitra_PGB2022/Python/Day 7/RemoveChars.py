str = input("Enter a string: ")
newStr = ""
for c in str:
    if(c.isdigit()):
        newStr += c
    else:
        pass

print(newStr)