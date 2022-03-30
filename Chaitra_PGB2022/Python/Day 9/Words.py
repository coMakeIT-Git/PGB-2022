import re

Name = input("Enter File Name: ")
path = "Files/" + Name
f = open(path, 'r')
text = f.read()
l = re.split('\s', text.strip())
while '' in l: l.remove('')
print("Word Count of", Name, ": ", len(l))