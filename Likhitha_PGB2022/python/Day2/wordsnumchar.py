str=input("Enter input string :")

res=[]

str2=str.split()

for i in str2:
    if any(char.isalpha() for char in i) and any(j.isdigit() for j in i):
        res.append(i)
        
print("Words containing both chracters and numbers in given string:",res)

