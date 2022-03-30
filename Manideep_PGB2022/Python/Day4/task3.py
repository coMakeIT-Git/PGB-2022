# Write a Python program that takes a text file as input and returns the number of words of a given text file.
# 	Note: Some words can be separated by a comma with no space.
import re
f=open('Day4/input.txt','r')
data=f.read()
k=re.split(r'[ ,]',data)  #split by space and comma
print(len(k))

f.close()