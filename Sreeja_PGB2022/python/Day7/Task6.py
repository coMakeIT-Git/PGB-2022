#Write a program to remove special symbols / punctuation from a string
from string import *
special='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
d=list(digits)
str1 = "/*We are le@arning python@67 fun_da**mentals**"

new_str=''
for i in str1:
    if i not in special and i not in d:
        new_str+=i
print(new_str)

#Write a program to removal all characters from a string except integers
str1 = 'I am 20 years and and 22 months old'
for i in str1:
    if i.isdigit():
        print(i,end='')
print()

#16. Write a program to find words with both alphabets and numbers from an input string.
str1 = "Sriman25 is Data scientist50 and AI Expert"
new_str=[]
for i in str1.split():
    d=a=False
    for j in i:
        if j.isalpha():
            a=True
        if j.isdigit():
            d=True
    if a and d:
        new_str.append(i)
print(new_str)

