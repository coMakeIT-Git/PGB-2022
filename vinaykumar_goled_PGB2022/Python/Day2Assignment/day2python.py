#Task 1:
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
res = calculation(40, 10)
print("Single function to add and subtract two numbers:")
print(res)

#Task 2:
def show_employee(name, salary = 9000):
    return name, salary
name = input("Enter your name:")
salary = input("Enter your salary:")
print(show_employee(name, salary))
print(show_employee("Harish"))

#Task 3:
def outer_func(num1, num2):
    def inner_func(num1, num2):
        return num1 + num2
    sum = inner_func(num1,num2)
    return sum + 5
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("Result: ", outer_func(num1, num2))

# Task 4:
def my_rec_func(n):
    if n:
        return n + my_rec_func(n - 1)
    else:
        return 0
T = my_rec_func(10)
print(T)

#Task 5:
def display_student(fname, curr_age):
    return fname, curr_age
print(display_student("John", 28))
show_student = display_student
print(show_student("David Miller", 30))

#Task 6:
mylist = []
size = int(input("Enter the size of the list:"))
print("Enter positive numbers:")
for i in range(size):
    data = int(input())
    mylist.append(data)
max = 0
for data in mylist:
    if data > max:
        max = data
print("The largest element in the list is: ", max)

#Task 7:
import datetime
date_time_str = 'March 10 2022 11:40AM'
date_time_object = datetime.datetime.strptime(date_time_str, '%B %d %Y %I:%M%p')
print(date_time_object)

#Task 8:
from datetime import date
from dateutil.relativedelta import relativedelta
four_months = date.today() + relativedelta(months=+4)
print("Date after four months from today: ",four_months)

#Task 9:
import random
otp = random.randint(000000, 999999)
print("OTP: ",otp)

#Task 10:
import random
import string
def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    for i in range(6):
        password += random.choice(random_source)
    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password
print("Generating a random password that is 10 characters long: ", get_random_password())

#Task 11:
print("Printing reverse number pattern")
rows = int(input("Enter number of rows: "))
for i in range(0, rows+1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

#Task 12:
string = input("Enter a string that contains letters, digits and special characters: ")
alphabets = digits = special = 0
for i in range(len(string)):
    if string[i].isalpha():
        alphabets = alphabets + 1
    elif string[i].isdigit():
        digits = digits + 1
    else:
        special = special + 1
print("\nTotal number of alphabets in the string: ", alphabets)
print("Total number of digits in the string: ", digits)
print("Total number of special symbols in the string: ", special)

#Task 13:
s1 = input("Enter a set of characters: ")
s2 = input("Enter some other set of characters: ")
s3 = ""
for i in range(len(s1)):
    s3 += s1[i]
    s3 += s2[-i-1]
print(s3)

#Task 14:
samp_str = input("Enter a sample string: ")
str_without_special_symbols = ""
for character in samp_str:
    if character.isalnum():
        str_without_special_symbols += character
print("String after removing special symbols and punctuation: ", str_without_special_symbols)

#Task 15:
str_with_numbers = input("Enter a string with numbers: ")
str_without_numbers = ""
for x in str_with_numbers:
    if x.isdigit():
        str_without_numbers += x
print("String after removing all characters except integers: ", str_without_numbers)

#Task 16:
string_with_alphanum = ["Sriman25 is Data scientist50 and AI Expert", "Num25 is greater than num20"]
print("Strings with both alphabets and numbers are: ")
for i in string_with_alphanum:
    for x in i.split(' '):
        if x.isalnum() and not x.isalpha() and not x.isdigit():
            print(x)

