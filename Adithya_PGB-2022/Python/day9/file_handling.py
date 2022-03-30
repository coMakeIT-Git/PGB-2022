import os
import csv
import shutil
#takes a text file as input and returns the number of words of a given text file
f=open("hi.txt","r")
data=f.readlines()
count=0
for i in data:
	i.replace(","," ")
	count+=len(i.split())
print(count)

#Removing newline characters from a file
f=open("hi.txt","r")
data=f.readlines()
l=[]
for i in data:
	l.append(i.strip("\n"))
print(l)

#copying the contents of a file to another file
f1=open("hi.txt")
f2=open("hello.txt","w")
if(os.path.exists("hello.txt")):
	os.rename("hello.txt","abc.txt")
for line in f1:
	f2.write(line)
f1.close()
f2.close()


#reading each row of a given csv file and skips the header of the file displays the number of rows and the field names
def csv_file():
    csvfile = input("Enter CSV File Name (csvfile.csv) : ")
    with open(csvfile, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        sum=0
        for line in reader:
        	print(line)
        	sum+=1
        print("Total Number of Rows : ",sum)
        print(f"feild Names : {headers}")

csv_file()
#displaying the file data such that every next character is separated by a symbol "#"
def count_hash():
    file = open("matter.txt","r")
    data = file.read()
    for letter in data:
        print(letter, end="#")

    file.close()
count_hash()
