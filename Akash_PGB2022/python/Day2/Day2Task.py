# Write a program to create function calculation()
def calculation(a, b):
    add = a + b
    sub = a - b
    return (add,sub)
result = calculation(10, 25)
print(result)


#Write a program to create a function show_employee()
#a. It should accept the employee’s name and salary and display both.
#b. If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name, salary=9000):
    print("Name is:", name, "salary is:", salary)

show_employee("Akash", 40000)
show_employee("Sai")
print("***********")

# Create an inner function to calculate the addition in the following way
#a. Create an outer function that will accept two parameters, a and b
#b. Create an inner function inside an outer function that will calculate the addition of a and b
#c. At last, an outer function will add 5 into addition and return it

# outer function
def outer(a, b):
    def inner(a, b):
        return a + b

    add = inner(a, b)
    return add + 5

result = outer(9,5)
print(result)
print("***********")

# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def recursive(number):
    if number:
        return number + recursive(number - 1)
    else:
        return 0

result = recursive(12)
print(result)
print("***********")


# Assign a different name to function and call it through the new name
#Ex: Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
def display_student(name, age):
    print(name, age)

display_student("Akash", 23)

showStudent = display_student

showStudent("Akash", 23)
print("***********")


# Find the largest item from a given list without using inbuilt methods
l = [1,2,6,5,8,12,55,46,32]
a=0
for i in l:
    if i>a:
        a=i
    else:
        a=a
print("Largest number in a list is:", a)
print("***********")


# Convert string into a datetime object
#Input : date_string = "Mar 09 2022 11:20AM"
#output: 2022-03-09 11:20:00
from datetime import datetime
from dateutil.relativedelta import relativedelta
date_string = "Mar 09 2022 11:20AM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)
print("***********")


# Calculate the date 4 months from the current date
today_date = datetime.now()
added_months = 4
new_date = today_date + relativedelta(months=+ added_months)
print("Date After adding 4Months:", new_date)
print("***********")


# Generate 6 digit random secure OTP
from random import  randint
print("YOUR OTP IS:")
for i in range(6):
    print(randint(0,10),end="")
print()
print("***********")


#Generate a random Password which meets the following conditions
#a. Password length must be 10 characters long.
#b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
import random
import string
character = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
password = ''.join(random.choice(character) for i in range(10))
print(password)
print("***********")


# Write a program to use for loop to print the following reverse number pattern
num = 5
for i in range(0,num+1):
    for j in range(num-i,0,-1):
        print(j,end=" ")
    print()
print("***********")


#Count all letters, digits, and special symbols from a given string
given_str = "akcu86k9ndh9@g#l!0ub&"
ltr_count = 0
digits_count = 0
symbol_count = 0

for i in given_str:
    if i.isalpha():
        ltr_count=ltr_count+1
    elif i.isdigit():
        digits_count=digits_count+1
    else:
        symbol_count=symbol_count+1
print("letters are: {}, Digits are: {}, symbols are: {}".format(ltr_count,digits_count,symbol_count))
print("***********")


#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
s1 = "comakeit"
s2 = "continuous"
new_str = ""
length = len(s1) if len(s1) > len(s2) else len(s2)
s2=s2[::-1]
for i in range(length):
    if i < len(s1):
        new_str=new_str+s1[i]
    if i < len(s2):
        new_str=new_str+s2[i]
print(new_str)
print("***********")


# Write a program to remove special symbols / punctuation from a string
#Ex : str1 = "/*We are le@arning python@67 fun_da**mentals**"
#Output: We are learning python fundamentals
str1 = "/*We are le@arning python@67 fun_da**mentals**"
new_str = ""
for letter in str1:
    if letter.isalpha():
        new_str=new_str+letter
    elif letter ==" ":
        new_str=new_str+letter
print((new_str))
print("***********")


#Write a program to removal all characters from a string except integers
#Input : str1 = 'I am 20 years and and 22 months old'
#Output : 2022
str1 = 'I am 20 years and and 22 months old'
new_str = ""
for num in str1:
    if num.isdigit():
        new_str=new_str+num
print((new_str))
print("***********")


#Write a program to find words with both alphabets and numbers from an input string.
#Input : str1 = "Sriman25 is Data scientist50 and AI Expert"
#Output : ['Sriman25','Scientist50']
str1 = "Sriman25 is Data scientist50 and AI Expert"
str1 =str1.split(" ")
new_str=[]
for i in str1:
    if any(y.isalpha() for y in i) and any(y.isdigit() for y in i):
        new_str.append(i)
print(new_str)
