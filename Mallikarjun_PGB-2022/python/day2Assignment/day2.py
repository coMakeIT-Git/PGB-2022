

#1- create function calculation() such that it can accept two variables

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

ans = calculation(100, 50)
print(ans)


#######################################################################

#2- create a function show_employee(),name and salary and display both,assign default value 9000 to salary

def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Mallikarjun", 12000)
show_employee("Vinay")


#############################################################

#3- inner function to calculate the addition

def outer_fun(a, b):
    multiply = a * b

    def addition(a, b):
        return a + b

    add = addition(a, b)
    return add + 5
output = outer_fun(10, 20)
print(output)


#####################################################################

#4- create a recursive function to calculate the sum of numbers from 0 to 10

def recurSum(n):
    if n <= 1:
        return n
    return n + recurSum(n - 1)
n = 10
print(recurSum(n))

#######################################################################

#5- different name to function and call it through the new name

def student(name, age):
    print(name, age)
student("Malli", 23)
newName =student
newName("Mallikarjun", 23)

######################################################################

#6- largest item from a given list without using inbuilt methods

list = [1,100,20,4,400,45,99]

print("Largest element is:", max(list))

#########################################################################

#7- Convert string into a datetime object

from datetime import datetime

def strtodate(strdate):
    return datetime.strptime(strdate,'%b %d %Y %I:%M%p')
print("Date is: ",strtodate("Mar 09 2022 11:20AM"))



###########################################################################

#8- the date 4 months from the current date

from datetime import date
from dateutil.relativedelta import relativedelta

four_months = date.today() + relativedelta(months=+4)
print(four_months)

###############################################################################

#9- 6 digit random secure OTP

import random

otp = random.randint(100000, 999999);

print("OTP:", otp);

###################################################################

#10-get random password pf length 10 with letters, digits, and symbols

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(10))
print("Random password is:", password)

##########################################################################

#11-reverse number pattern

rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

##############################################################################

#12-Count all letters, digits, and special symbols from a given string

string = "le@rn1ng Pyth0n !$ E@$Y"
alphabets = digits = special = 0

for i in range(len(string)):
    if (string[i].isalpha()):
        alphabets = alphabets + 1
    elif (string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1

print("\nTotal Number of Letters in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)

#################################################################################

#13- two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
# then the last char of s2, Next, the second char of s1 and second last char of s2, and
# so on. Any leftover chars go at the end of the result

str1=("Malli")
str2=("Karjun")
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


###########################################################################

#14- to remove punctuation from a given string


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str = "/*We are le@arning python@67 fun_da**mentals**"

no_punct = ""
for char in str:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)

####################################################################

#15- Write a program to removal all characters from a string except integers

def remove_chars(str):
    newstr=""
    for i in str:
        if i.isdigit():
            newstr+=i
    print("After removing all characters from string:",newstr)
str="I am 20 years and and 22 months old"
remove_chars(str)

##################################################################################

#16- Write a program to find words with both alphabets and numbers from an input string.



def func(s):
    alpha=digit=0
    for i in s:
        if(i.isdigit()):
            digit+=1
        elif(i.isalpha()):
            alpha+=1
    if(digit>0and alpha>1):
        return True
    return False

def find_pattern(s):
    s=s.split()
    l=[]
    for i in s:
        if(func(i)==True):l.append(i)
    print(l)
find_pattern("Sriman25 is Data scientist50 and AI Expert")

