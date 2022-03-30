#Reverse number pattern
n=int(input("Enter number of rows"))
for i in range(0,n):
    k=n-i
    for j in range(k,0,-1):
        print(j,end=" ")
    print()

#Count all letters, digits, and special symbols from a given string
def count(str):
    letter_count=0
    digits_count=0
    symbols_count=0
    for i in str:
        if(i.isalpha()):
            letter_count+=1
        elif(i.isalnum()):
            digits_count+=1
        else:
            symbols_count+=1
    print("Number of letters in string:",letter_count)
    print("Number of digits in string:", digits_count)
    print("Number of special symbols in string:", symbols_count)
str=input("Enter any string value")
count(str)

#Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
str1=input("Enter first string value:")
str2=input("Enter second string value:")
len1=len(str1)
len2=len(str2)
str2=str2[::-1]
length=min(len1,len2)
print(length)
str3=""
for i in range(0,length):
    str3=str3+str1[i]
    str3=str3+str2[i]
#print(str3)
for i in range(length,len(str1)):
    str3=str3+str1[i]
for i in range(length,len(str2)):
    str3=str3+str2[i]
print(str3)

# Write a program to remove special symbols / punctuation from a string
def remove(str):
    newstr=""
    for i in str:
        if i.isalpha() or i.isspace():
            newstr+=i
    print("After removing punctuation and special symbols:",newstr)
str="/*We are le@arning python@67 fun_da**mentals**"
remove(str)

# program to removal all characters from a string except integers
def remove_chars(str):
    newstr=""
    for i in str:
        if i.isdigit():
            newstr+=i
    print("After removing all characters from string:",newstr)
str="I am 20 years and and 22 months old"
remove_chars(str)

#find words with both alphabets and numbers from an input string
def alphanumString(str):
    l=str.split()
    l2=[]
    for x in l:
        if x.isalnum() and not(x.isalpha() or x.isdigit()):
            l2.append(x)
    return l2
print(alphanumString("Sriman25 is Data scientist50 and AI Expert"))

