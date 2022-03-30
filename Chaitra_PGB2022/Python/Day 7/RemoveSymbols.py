def isSymbol(c):
    if c.isalpha():
        return False
    elif c.isdigit():
        return True
    elif c == " ":
        return False
    else:
        return True

str = input("Enter a string: ")
newStr = ""
for c in str:
    if(isSymbol(c)):
        pass
    else:
        newStr += c

print(newStr)
