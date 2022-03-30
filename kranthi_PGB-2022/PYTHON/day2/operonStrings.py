#Write a program to remove special symbols / punctuation from a string

str3="/*We are le@arning python@67 fun_da**mentals**"
j=len(str3)
s_res=""
for i in range(j):
    if(str3[i].isalpha()):
        s_res+=str3[i]
print("a program to remove special symbols / punctuation from a string:")
print(s_res)

#Write a program to removal all characters from a string except integers

str4="I am 20 years and and 22 months old"
k=len(str4)
s_res1=""
for i in range(len(str4)):
    if(str4[i].isdigit()):
        s_res1+=str4[i]
print("a program to removal all characters from a string except integers:")
print(s_res1)

#Write a program to find words with both alphabets and numbers from an input string.
print("a program to find words with both alphabets and numbers from an input string")
str5="Sriman25 is Data scientist50 and AI Expert"
li=str5.split(" ")
li1=[]
for i in range(len(li)):
    if(not li[i].isalpha() or li[i].isdecimal()):
        li1.append(li[i])
print(li1)