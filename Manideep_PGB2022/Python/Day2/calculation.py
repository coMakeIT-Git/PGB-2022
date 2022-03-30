from  datetime import datetime
from dateutil.relativedelta import *
import random
from string import *


special=['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
upper=list(ascii_uppercase)
lower=list(ascii_lowercase)
digi=list(digits) 

# Write a program to create function calculation() such that it can accept two variables 
# and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
def calculation(a,b):
    return a+b,a-b

s=calculation(2,4)
print("sum is {} Difference is {}".format(s[0],s[1]))

# Write a program to create a function show_employee() using the following conditions.
# 	a. It should accept the employee’s name and salary and display both.
# 	b. If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name,salary=9000):
    print('Employee Name is {} \n Employee salary is {}'.format(name,salary))
show_employee('Manideep')
show_employee('Manideep',10000)

# Create an inner function to calculate the addition in the following way
# 	a. Create an outer function that will accept two parameters, a and b
# 	b. Create an inner function inside an outer function that will calculate the addition of a and b
# 	c. At last, an outer function will add 5 into addition and return it
def outer(a,b):
    def inner(a,b):
        return a+b
    return inner(a,b)

print(outer(5,7))
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def recursivesum(a=10):
    if a<=1:
        return a
    return a+recursivesum(a-1)
print(recursivesum())

# Assign a different name to function and call it through the new name
# 	Ex: Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
def display_student(name, age):
    return 'Name is {} \n Age is {}'.format(name,age)
a=display_student
print(a('Manideep',21))

# largest number in list 
def findlargest(l):
    r=l[0]
    for i in l:
        if i>r:
            r=i
    return r

print(findlargest([12,24,35,121,-12,112]))

# Convert string into a datetime object
# 	Input : date_string = "Mar 09 2022 11:20AM"
# 	output: 2022-03-09 11:20:00

print(datetime.strptime("Mar 09 2022 11:20AM", '%b %d %Y %I:%M%p'))

current_date=datetime.now()
updateddate = current_date + relativedelta(months=+4)
print(updateddate)

# Generate 6 digit random secure OTP
def getOTP():
    c=''
    for i in range(6):
        c+=str(random.randint(0,9))
    return c
print(getOTP())

# Generate a random Password which meets the following conditions
# 	a. Password length must be 10 characters long.
# 	b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
def getpassword():
    
    n=10
    randomuppercount=random.randint(2,n-2)
    randomdigitscount=random.randint(1,n-randomuppercount-1)
    randomspecialcounts=random.randint(1,n-randomuppercount-randomdigitscount)
    randomlowercount=n-randomspecialcounts-randomdigitscount-randomuppercount
    password=[]
    for i in range(randomuppercount):
        password.append(random.choice(upper))
    for i in range(randomdigitscount):
        password.append(random.choice(digi))
    for i in range(randomspecialcounts):
        password.append(random.choice(special))
    for i in range(randomlowercount):
        password.append(random.choice(lower))
    random.shuffle(password)
    return ''.join(password)

print(getpassword())

#  Write a program to use for loop to print the following reverse number pattern
for i in range(5,-1,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

#Count all letters, digits, and special symbols from a given string

st=input('Enter a String')
l=d=s=0
for i in st:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1
    elif i in special:
        s+=1
print('Count of Letters : {} \n Count of Digits: {} \n Count of special charcters :{}'.format(l,d,s))


# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, 
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
s1=ascii_lowercase
s2=ascii_uppercase
s3=''
for i in range(26):
    s3+=s1[i]+s2[-(i+1)]
print(s3)



#  Write a program to remove special symbols / punctuation from a string
# 	Ex : str1 = "/*We are le@arning python@67 fun_da**mentals**"
# 	Output: We are learning python fundamentals
str1 = "/*We are le@arning python@67 fun_da**mentals**"

new_str=''
for i in str1:
    if i not in special and i not in digi:
        new_str+=i
print(new_str)

# Write a program to removal all characters from a string except integers
# 	Input : str1 = 'I am 20 years and and 22 months old'
# 	Output : 2022

str1 = 'I am 20 years and and 22 months old'
for i in str1:
    if i.isdigit():
        print(i,end='')
print()
#  Write a program to find words with both alphabets and numbers from an input string.
# 	Input : str1 = "Sriman25 is Data scientist50 and AI Expert"
# 	Output : ['Sriman25','Scientist50']

str1 = "Sriman25 is Data scientist50 and AI Expert"
l=[]
for i in str1.split():
    d=a=False
    for j in i:
        if j.isalpha():
            a=True
        if j.isdigit():
            d=True
    if a and d:
        l.append(i)
print(l)


