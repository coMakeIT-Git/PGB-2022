import random
import string
length=int(input("enter password length:"))
nums=string.digits
caps=string.ascii_uppercase
small=string.ascii_lowercase
special=string.punctuation
temp=nums+caps+small+special
result=random.sample(temp,length)
password="".join(result)
print(password)

