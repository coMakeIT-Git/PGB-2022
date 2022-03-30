"""
1.Write a program to create function calculation() such that it can accept two variables and
calculate addition and subtraction. Also, it must return both addition and subtraction in a single
return call.

function:   In Python a function is defined using the def keyword

pass statement: function definitions cannot be empty, but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.
Taking input in Python using :
1.input() : This function first takes the input from the user and then evaluates the expression.
"""
def calculator(a,b):
    c=a+b
    d=a-b
    return c,d
res=calculator(5,4)
print("Addition and subtraction: ",res)
"""
2. Write a program to create a function show_employee() using the following conditions.
	a. It should accept the employee’s name and salary and display both.
	b. If the salary is missing in the function call then assign default value 9000 to salary
"""
def show_employee(empname,empsalary=9000):
    return empname,empsalary


empname= "Pritam"
empsalary="99999999999999999999999999999999999999999"

print("Employee name and salary :",show_employee(empname,empsalary))
"""
3.Create an inner function to calculate the addition in the following way
	a. Create an outer function that will accept two parameters, a and b
	b. Create an inner function inside an outer function that will calculate the addition of a and b
	c. At last, an outer function will add 5 into addition and return it
"""
def Outerfun(a,b):
    def innerfun():
        return a+b
    return 5+innerfun()

print("Outer function: ",Outerfun(5,4))

"""
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

adv recursive function:
    1.Recursive functions make the code look clean and elegant.
    2.A complex task can be broken down into simpler sub-problems using recursion.
    3.Sequence generation is easier with recursion than using some nested iteration.

dis recursive function:
    1.Sometimes the logic behind recursion is hard to follow through.
    2.Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
    3.Recursive functions are hard to debug.
"""
def sum(n):
    if n < 1:
        return n
    return n+sum(n-1)
print("The sum of number 0 to 10 :",sum(10))
"""
Assign a different name to function and call it through the new name
	Ex: Below is the function display_student(name, age). 
	Assign a new name show_tudent(name, age) to it and call it using the new name.
"""
def display_student(name, age):
    print(name, age)

# call using original name
display_student("Pritam", 22)

# assign new name
showStudent = display_student
# call using new name
showStudent("Pritam", 22)

"""
Find the largest item from a given list without using inbuilt methods
"""
Numbers = [90,78,34,50,100,99]
higest_number = 0
for number in Numbers:
    if number > higest_number:
        higest_number = number
"""
Convert string into a datetime object
	Input : date_string = "Mar 09 2022 11:20AM"
	output: 2022-03-09 11:20:00	
"""
import datetime
date_time_str = 'Mar 09 2022 11:20AM'
date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
print('Date-time:', date_time_obj)
"""
Calculate the date 4 months from the current date
"""
import datetime
print((datetime.date.today() + datetime.timedelta(4*365/12)).isoformat())
# 2018-09-24 13:24:04.007620
"""
Generate 6 digit random secure OTP
"""
import random
otp = random.randint(100000, 999999);
print("OTP:", otp);
"""
 Generate a random Password which meets the following conditions
	a. Password length must be 10 characters long.
	b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
"""
import random
import string

# uchars = Uppercase charaters
# lchars =  Lowercase charaters
# dchars = Digits
# schars = Punctuation or Special Charaters

def get_random_string(uchars = 2, lchars = 6, dchars = 1, schars = 1):
    # Generates a 10 characters long random string
    # with 2 upper case, 6 lowe case, 1 digits and 1 special characters

    str_uchars, str_lchars, str_dchars, str_schars = '', '', '', ''

    for i in range(uchars):
        str_uchars += random.SystemRandom().choice(string.ascii_uppercase)

    for i in range(lchars):
        str_uchars += random.SystemRandom().choice(string.ascii_lowercase)

    for i in range(dchars):
        str_uchars += random.SystemRandom().choice(string.digits)

    for i in range(schars):
        str_uchars += random.SystemRandom().choice(string.punctuation)

    random_str = str_uchars + str_lchars + str_dchars + str_schars
    random_str = ''.join(random.sample(random_str, len(random_str)))
    return random_str



# generates 2 uppercase,  6 lowercase, 1 digits and 1 punctuation
print('Your Random Password:', get_random_string(2, 6, 1, 1))

"""
Write a program to use for loop to print the following reverse number pattern
        5 4 3 2 1 
		4 3 2 1 
		3 2 1 
		2 1 
		1
	h. Return a set that contains all items from both sets, duplicates are excluded
	i. Insert the items from set y into set x
"""
print("reverse number pattern:")
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
"""
Count all letters, digits, and special symbols from a given string
"""
str1 = input("Please Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(str1)):
    if (ord(str1[i]) >= 48 and ord(str1[i]) <= 57):
        digits = digits + 1
    elif ((ord(str1[i]) >= 65 and ord(str1[i]) <= 90) or (ord(str1[i]) >= 97 and ord(str1[i]) <= 122)):
        alphabets = alphabets + 1
    else:
        special = special + 1

print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)
"""
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
Any leftover chars go at the end of the result.
"""
s1="Pritam"
s2="biswas"
length1=len(s1)
length2=len(s2)
if length1>length2:
    length=length1
else:
    length=length2
s2=s2[::-1]
s3=""
for i in range(length):
    if i < length1:
        s3 = s3 + s1[i]
    if i < length2:
        s3 = s3 + s2[i]
print(s3)
"""
Write a program to remove special symbols / punctuation from a string
	Ex : str1 = 
	Output: We are learning python fundamentals
"""
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "/*We are le@arning python@67 fun_da**mentals**"
# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char
# display the unpunctuated string
print("Display the unpunctuated string: ",no_punct)

"""
Write a program to removal all characters from a string except integers
	Input : str1 = 'I am 20 years and and 22 months old'
	Output : 2022
"""
str1 = 'I am 20 years and and 22 months old'
print("initial string : ", str1)
getVals = list([val for val in str1 if val.isnumeric()])
result = "".join(getVals)
print("final string:", result)

"""
Write a program to find words with both alphabets and numbers from an input string.
	Input : str1 = "Sriman25 is Data scientist50 and AI Expert"
	Output : ['Sriman25','Scientist50']
"""

str12 = "Sriman25 is Data scientist50 and AI Expert"
print("The original string is : " + str12)
res = []
temp =str12.split()
for idx in temp:
    if any(chr.isalpha() for chr in idx) and any(chr.isdigit() for chr in idx):
        res.append(idx)
print("Words with alphabets and numbers : " + str(res))
