str1=input("Enter string1 :")
str2=input("Enter string2 :")

k=len(str1)
l=len(str2)

str2 = str2[::-1]
str3=""
if k>l :
    len=k
else:
    len=l
    
for i in range(len):
    if(i<k):
        str3 = str3+str1[i]
    if(i<l):
        str3=str3+str2[i]
    
print("Output String",str3)