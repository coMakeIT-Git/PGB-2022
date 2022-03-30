str="welcome to the world of programming"
print("string converted to upper case:")
print(str.upper())
print("\n")

print("String converted to lower case:")
print(str.lower())
print("\n")
print("String Converted to title strating words are capital:)")
print(str.title())
print("Number of times 'o' occured : ",str.count('o'))
print("\n")
print("last character checking:")
if(str[-1]=='g'):
    print(True)
print('''Since string contains " "  str.isalpha() returns false:''')
print(str.isalpha())
print("first charater of the string converted to capital:")
print(str.capitalize())
print("program to get position of a char in a string")
r="p"
res = None
for i in range(0,len(str)):
    if(str[i]==r):
        res=i+1
        break
if (res==None):
    print("no such character exists")
else:
    print("the character {} is present at {}".format(r,res))
print("Reverse of string using slice:")
print(str[len(str)::-1])

