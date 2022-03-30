import csv
#Write a Python program that takes a text file as input and returns the number of words of a given text file.
	#Note: Some words can be separated by a comma with no space.

def count_words(filepath):
    a=open(filepath,"r+")
    b=a.read()
    b=b.replace(","," ")
    b=b.replace("\n"," ")
    b=b.split(" ")
    print("the number of words of a given text file is:",len(b))
a=input("Enter a file with path in your PC:")
count_words(a)
print("###########")

# Write a Python program to remove newline characters from a file
def remove_line(filepath):
    a1 = open(filepath, "r+")
    b1 = a1.read()
    b1 = b1.replace("\n", " ")
    print("removed newline characters:",b1)
remove_line("demo.txt")
print("###########")

# Write a Python program to copy the contents of a file to another file
def copying_file(fromfilepath,tofilepath):
    with open(fromfilepath,"r") as f1, open(tofilepath,"w") as f2:
        for x in f1:
            f2.write(x)
    a=open("demo2.txt")
    b=a.read()
    print("******files are copied*****")
    print("Data in copied file:\n",b)
copying_file("demo.txt","demo2.txt")
print("#########")

# Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.

with open('democsv.csv',"r") as file:
    csvFile = csv.reader(file,delimiter = ',')
    field=[]
    header=next(csvFile)
    c=0
    for lines in csvFile:
        print(lines)
        c=c+1
    for row in header:
        field.append(row)
    print("The field names are:",field)
    print("the number of rows without header:",c)
print("#############")

# A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#".
	#Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.

def hash_code():
    a=open("matter.txt","r")
    b=a.read()
    for x in b:
        print(x,end="#")
hash_code()


