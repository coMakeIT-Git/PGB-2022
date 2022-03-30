from datetime import date
from datetime import datetime
from random import randint
import string
import random
from dateutil.relativedelta import relativedelta


#program to create function calculation() such that it can accept two variables and calculate addition and subtraction.
def calculate(x,y):
	add = x+y
	sub = x-y
	return add,sub
print("addition and subtraction: ", calculate(15345, 523))
print()


#Write a program to create a function show_employee()
def show_employee(name,sal=9000):
	print("Emplayee Name: ",name," Salary: ",sal)
show_employee("Vinay")
show_employee("RAM", 35000)
print()


#Create an outer function that will accept two parameters, a and b
#Create an inner function inside an outer function that will calculate the addition of a and b	
def outerFunc(a,b):
	def innerFunc():
		return a+b
	return innerFunc()+5
print("calculate addition using inner function: ", outerFunc(10, 15))
print()


#recursive function for sum of  number 0-10
def addNums(n):
	if n==0:
		return 0
	else:
		return n+addNums(n-1)
print("sum  using recursive function:",addNums(10))
print()

		
#Assign a different name to function and call it through the new name
def showdetails(name,n):
	print(name,n)
showaccountdetails = showdetails
showaccountdetails("Darwin",245243526)


#Find the largest item from a given list without using inbuilt methods
def maxval(lst):
	mx = lst[0]
	for i in lst:
		if i>mx:
			mx = i
	return mx
print("Max element: ",maxval([5,9,8,4,23,45,19,21,11,78,22]))


#Convert string into a datetime object
def strtodate(s):
	return datetime.strptime(s, '%b %d %Y %I:%M%p')
print(strtodate("Mar 09 2022 11:20AM"))	


#Calculate the date 4 months from the current date 
def dateFunc():
	return date.today()+relativedelta(months=+4)
print("Date after 4 months: ",dateFunc())


#Generate 6 digit random secure OTP
def genOTP():
	otp = randint(10**5,(10**6)-1)
	return 	otp
print(genOTP())


#Generate a random Password
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


#PATTERN
def pattern():
	for i in range(5):
		for j in range(5-i,0,-1):
			print(j,end=" ")
		print()
	

#Count all letters, digits, and special symbols from a given string
def count(s):
	nums = 0
	alpbt = 0
	symbl = 0
	for i in s:
		if i.isalpha():
			alpbt += 1
		elif i.isdigit():
			nums += 1
		else: 
			symbl += 1		
	return nums,alpbt,symbl


#Adding characters to third String
def strings(s1,s2):
	s2 = s2[::-1]
	l = min(len(s1),len(s2))
	s = ""
	for i in range(l):
		s += s1[i]+s2[i]
	s += s1[l:]
	s += s2[l:]
	print(s)
strings("Akhil","Balaji")


#Write a program to remove special symbols / punctuation from a string
def removesymbols(s):
	s1 = ""
	for i in s:
		if i.isalnum() or i.isspace():
			s1 += i
	return s1
print(removesymbols("/*We are le@arning python@67 fun_da**mentals**"))


#Write a program to removal all characters from a string except integers
def removeChars(s):
	s1 = ""
	for i in s:
		if i.isdigit():
			s1 += i
	return s1
print(removeChars('I am 20 years and and 22 months old'))


#Write a program to find words with both alphabets and numbers from an input string
def alphanumString(s):
	l = s.split()
	l2 = []
	for x in l:
		if x.isalnum() and not(x.isalpha() or x.isdigit()):
			l2.append(x)
	return l2	
print(alphanumString("Sriman25 is Data scientist50 and AI Expert"))
	
	
	
	
	
