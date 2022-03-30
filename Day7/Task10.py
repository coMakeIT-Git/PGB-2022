 #Generate a random Password which meets the following conditions
	#a. Password length must be 10 characters long.
	#b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
import random
import string
length=int(input("enter password length"))
nums=string.digits
caps=string.ascii_uppercase
small=string.ascii_lowercase
special=string.punctuation
temp=nums+caps+small+special
result=random.sample(temp,length)
password="".join(result)
print(password)