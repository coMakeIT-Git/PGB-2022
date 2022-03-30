# Write a Python program to remove newline characters from a file

import os.path
from os import path
import re



f=open('Day4/input.txt','r')
data=f.read()
print(data)         
l=data.replace('\n','')  #Replace New line characters
print(l)
f.close()


# 5. Write a Python program to copy the contents of a file to another file .


f1=open('Day4/input.txt','r')
data=f1.read()
print(data)
file_name=input("Please Enter filename to copy data\n")
if path.exists('Day4/'+file_name):
    print(f"{file_name} already exists")
else:
    f2=open('Day4/'+file_name,'w')
    f2.write(data)
f1.close()
f2.close()