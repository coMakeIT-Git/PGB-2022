# 1 Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction.
#Also, it must return both addition and subtraction in a single return call.

def calculation(num1,num2):
    add=num1+num2
    sub=num1-num2
    return add,sub
print(calculation(10,2))

#####################################################
#2 Write a program to create a function show_employee() using the following conditions.
#a. It should accept the employee’s name and salary and display both.
#b. If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)
show_employee("upendar", 12000)
show_employee("rakesh")


###########################################################
# 3 Create an inner function to calculate the addition in the following way
# 	a. Create an outer function that will accept two parameters, a and b
# 	b. Create an inner function inside an outer function that will calculate the addition of a and b
# 	c. At last, an outer function will add 5 into addition and return it

def outer_fun(a, b):            # outer function

    def addition(a, b):          # inner function
        return a + b
    add = addition(a, b)            # call inner function from outer function
    return add + 5
result = outer_fun(5, 10)
print(result)


########################################################
# 4. Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def recursive(n):
    if n <= 1:
        return n
    return n + recursive(n - 1)
n = 10
print(recursive(n))

######################################################
# 5 Assign a different name to function and call it through the new name

def student(name, age):
    return(name, age)
student("rakesh", 26)
student1 =student                        # assign new name
print(student1("rakesh", 26))            # call using new name


######################################################
# 6 Find the largest item from a given list without using inbuilt methods
def maxlist(list1):
    max = list1[0]
    for x in list1:
        if x > max :
            max = x
    return max
list1 = [10,9,21,3,11]
print("Largest element is:", maxlist(list1))
###########################################################
# 7 Convert string into a datetime object
import datetime
datetime_object = datetime.datetime.strptime('Mar 09 2022 11:20AM', '%b %d %Y %I:%M%p')
print(datetime_object)

##################################################
# 8 Calculate the date 4 months from the current date
import datetime
print (datetime.date.today() + datetime.timedelta(4*365/12))

#######################################################
# 9 Generate 6 digit random secure OTP

import random
otp = random.randint(100000, 999999)
print("RandomOTP is:", otp)

#######################################################
# 10 Generate a random Password which meets the following conditions

import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(10))
password = random.sample(characters, 6)
password += random.sample(string.ascii_uppercase, 2)     # 2 upperkeys
password += random.choice(string.digits)                 # 1 digit
password += random.choice(string.punctuation)            # 1 symbol
password=''.join(password)
print("Random password is:", password)

########################################################################
# 11 Write a program to use for loop to print the following reverse number pattern

rows = int(5)
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

######################################################
 # 12 Count all letters, digits, and special symbols from a given string

string = "rowdy@123"                     ## Take the Input From the User
alphabets = digits = special = 0
for i in range(len(string)):               ##count alphabets
    if (string[i].isalpha()):
        alphabets = alphabets + 1
    elif (string[i].isdigit()):             # count digits
        digits = digits + 1
    else:
        special = special + 1               # count special symbols
print("\nTotal Number of Alphabets in this String:  ", alphabets)
print("Total Number of Digits in this String:  ", digits)
print("Total Number of Special Characters in this String:  ", special)

############################################################
# 13 Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.
s1 = "upendar"
s2 = "varun"
s1_length = len(s1)         # get string length
s2_length = len(s2)

length = s1_length if s1_length > s2_length else s2_length
result = ""
s2 = s2[::-1]                # reversing string 2

for i in range(length):
    if i < s1_length:
        result = result + s1[i]     #string1 first
    if i < s2_length:
        result = result + s2[i]      #string2 first after reversing
print(result)

###############################################################################
# 14 Write a program to remove special symbols / punctuation from a string

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''               # define punctuation
str = "/*We are le@arning python@67 fun_da**mentals**"

no_punct = ""                                                   # remove punctuation from the string
for char in str:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)

###########################################################################
# 15 Write a program to removal all characters from a string except integers
str = 'I am 20 years and and 22 months old'
str=''.join(i for i in str if i.isdigit())
print(str)

##################################################################
# 16 Write a program to find words with both alphabets and numbers from an input string

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

#######################################################################