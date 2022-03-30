#Count all letters, digits, and special symbols from a given string
inp=input("Enter a string")
num=len(inp)
count1=0
count2=0
count3=0
for i in range(num):
    if(inp[i].isalpha()):
        count1=count1+1
    elif(inp[i].isdigit()):
        count2=count2+1
    else:
        count3=count3+1
print("Alphabets count",count1,"digits count",count2,"special charcaters count",count3)