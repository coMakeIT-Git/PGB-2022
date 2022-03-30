import re
import csv
#take a text file as input and return the number of words of a given text file.
f = open("test")
data = f.read()
reg = r'[, ]'
wrds = len(re.split(reg, data))
print("number of words in file:",wrds)


#Python program to remove newline characters from a file
def removeNewline():
	dt = open("test").readlines()
	return [x.rstrip('\n') for x in dt]
f = open("updated","w")
f.write(' '.join(removeNewline()))


#Python program to copy the contents of a file to another file
with open("test","r") as f1, open("updates","w") as f2:
	for l in f1:
		f2.write(l)
		
		
#Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.
with open("color.csv") as cf:
	dt = csv.reader(cf)
	rws = 0
	flds = next(dt)
	print("CSV data: ")
	for l in dt:
		rws += 1
		print(' '.join(l))
	print("No of rows:",rws)
	print("Fields Names:",' '.join(flds))


#Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
def hash_display():
	file = open("test","r")
	data = file.read()
	for letter in data:
		print(letter, end="#")
	file.close()
hash_display()
