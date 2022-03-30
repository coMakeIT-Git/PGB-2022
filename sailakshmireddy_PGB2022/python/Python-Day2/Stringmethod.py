# Count all letters, digits, and special symbols from a given string
a="euygfsubxi7201!@#$!@@#%"
letters_count=0
digits_count=0
symbol_count=0
for x in a:
    if x.isalpha():
        letters_count=letters_count+1
    elif x.isdigit():
        digits_count=digits_count+1
    else:
        symbol_count=symbol_count+1
print("letter are:{},digits are:{},symbols are:{}".format(letters_count,digits_count,symbol_count))
print("#######")

# Write a program to create a new string s3 made of the first char of s1,
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
# any leftover chars go at the end of the result.
s1="apple"
s2="pineapple"
s3=""
length = len(s1) if len(s1)> len(s2) else len(s2)
s2 = s2[::-1]
for i in range(length):
    if i < len(s1):
        s3=s3+s1[i]
    if i < len(s2):
        s3=s3+s2[i]
print("New string is:",s3)
print("######")

#Write a program to remove special symbols / punctuation from a string
str= "/*We are le@arning python@67 fun_da**mentals**"
s1=""
for x in str:
    if x.isalpha():
        s1=s1+x
    elif x==" ":
        s1=s1+x
print("after removing a symbols / punctuation:",s1)
print("##########")

# Write a program to removal all characters from a string except integers
str='I am 20 years and and 22 months old'
str1=""
for x in str:
    if x.isdigit():
        str1=str1+x
print("integers in string are: ",str1)
print("##########")

# Write a program to find words with both alphabets and numbers from an input string.
str="Sriman25 is Data scientist50 and AI Expert"
str=str.split(" ")
str1=[]
for x in str:
    if any(y.isalpha() for y in x) and any(y.isdigit() for y in x):
        str1.append(x)
print(str1)




