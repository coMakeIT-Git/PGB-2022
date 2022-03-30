str=input("Enter input string :")

res=""
for i in range(len(str)):
    if(str[i].isdigit()):
        res=res+str[i]
        
        
print("String after removing all characters :",res)
    