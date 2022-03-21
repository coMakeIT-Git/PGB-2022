#returns the number of words of a given text file.
import shutil
import os

file=open("Text.txt")
#print(file.read())
num=0
count=0
for line in file:
    line=line.replace(","," ")
    words=line.split()
    print(words)
    num+=len(words)
print("Total number of words in a file are:",num)
file.close()

#remove newline characters from a file

def newline():
    f1 = open("Text.txt").readlines()
    return [s.rstrip('\n') for s in f1]


print(newline())


#copy the contents of a file to another file
with open("Text.txt",'r') as file1,open("destination.txt",'w') as file2:
    if (os.path.exists("destination.txt")):
        os.rename("destination.txt","Myfile.txt")
    for line in file1:
        file2.write(line)
    print("Files are copied from the Text file to destination")

#shutil.copyfile("Text.txt","destination.txt")
file.close()


#print the number of rows and the field names.
from csv import reader
import pandas as pd
results=pd.read_csv("Sample.csv")
print("Total Number Of Rows are ",len(results))
fields=[]
data=reader(results)
fields=next(data)
for field in fields:
    print(field)


# every next character is separated by a symbol "#"
def hash_display():
    with open("matter.txt") as file:
        data=file.read()
    for letter in data:
        print(letter,end='#')
    file.close()

hash_display()
