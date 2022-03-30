def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub

print("addition and subtraction: ", calculation(15, 5))
print()

#--------------------------------------------------------------------

def show_employee(name, salary=9000):
    print("employee name:", name, " salary:", salary)

show_employee("nithish", 15000)
show_employee("kumar")
print()

#---------------------------------------------------------------------

def outer(a, b):
    def inner():
        return a + b

    return inner() + 5

print("calculate addition using inner function: ", outer(10, 15))
print()

#-----------------------------------------------------------------------
#recursive function for sum of  number 1-10

def rec_fun(n):
    if(n<=1):
        return n
    else:
        return n+rec_fun(n-1)

print("sum of 1-10 using recursive function:",rec_fun(10))
print()

#-------------------------------------------------------------------------
#Assigning a different name to function and calling it through the new name

display_employee=show_employee
display_employee("akhil",8000)
print()

#--------------------------------------------------------------------------
#printing largest item from a given list without using inbuilt methods

list=[5,9,8,4,23,45]
def largest(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    print("largest item in list:",max)

largest(list)
print()

#----------------------------------------------------------------------------
#Converting string into a datetime object

import datetime
from dateutil.relativedelta import relativedelta

def date_convert(date_string):
    date_time = datetime.datetime.strptime(date_string, '%b %d %Y %I:%M%p')
    print(date_time)

date_convert("Mar 10 2022 11:25AM")
print()

#Calculating the date 4 months from the current date

def date_move():
    cur_date = datetime.date.today()
    return cur_date + relativedelta(months=4)

print("date after 4 months from now:",date_move())
print()

#--------------------------------------------------------------------------------
#random otp

import random
import string

def rand():
    otp = random.randint(100000, 999999)
    return otp

print("Random otp:", rand())
print()


#random string password

def rand_pass():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    password = random.sample(characters, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    password = ''.join(password)
    return password

print("random password:",rand_pass())
print()

#------------------------------------------------------------------------------------------
#pattern printing

def pattern():
    for i in range(0,5):
        for j in range(5-i,0,-1):
            print(j,end=" ")
        print()

print("pattern: ")
pattern()
print()


#--------------------------------------------------------------------------------------------
#counting letter,digits,special symbol

def count(s1):
    alpha=0
    num=0
    special=0
    for i in s1:
        if(i.isalpha()):
            alpha+=1
        elif(i.isdigit()):
            num+=1
        else:
            special+=1
    print("letters count:",alpha)
    print("numbers count:",num)
    print("special symbol count:",special)



s1="cont1nuou$ innov@tion123"
count(s1)
print()

#-----------------------------------------------------------------------------------------------------
#program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

def program(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    str2 = str2[::-1]
    length = min(len1, len2)
    str3 = ""
    for i in range(0, length):
        str3 = str3 + str1[i]
        str3 = str3 + str2[i]
    for i in range(length, len(str1)):
        str3 = str3 + str1[i]
    for i in range(length, len(str2)):
        str3 = str3 + str2[i]
    return str3

str1 = "akhil"
str2 = "balaji"
print("result string:",program(str1,str2))
print()

#----------------------------------------------------------------------------------------------------------------
#program to remove special symbols / punctuation from a string

def removesymbols(s):
	s1=""
	for i in s:
		if(i.isalnum() or i.isspace()):
			s1+=i
	return s1

s="/*We are le@arning python@67 fun_da**mentals**"
print("result string after removing special symbols:",removesymbols(s))
print()

#-----------------------------------------------------------------------------------------------------------------
#program to removal all characters from a string except integers

def removeChars(s):
	s1=""
	for i in s:
		if i.isdigit():
			s1+=i
	return s1

s="I am 20 years and and 22 months old"
print("result string after removal of all characters from a string except integers:",removeChars(s))
print()


#-------------------------------------------------------------------------------------------------------------------
#program to find words with both alphabets and numbers from an input string.

def alphanumString(s):
    l=s.split()
    l2=[]
    for x in l:
        if x.isalnum() and not(x.isalpha() or x.isdigit()):
            l2.append(x)
    return l2

s="Sriman25 is Data scientist50 and AI Expert"
print("result list after finding both aplhabets and numbers from string:",alphanumString(s))


