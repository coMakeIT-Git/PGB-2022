import csv
#Write a Python program that takes a text file as input and returns the number of words of a given text file.
	#Note: Some words can be separated by a comma with no space.
def count_words(filepath):
    a=open(filepath,"r+")
    b=a.read()
    b=b.replace(","," ")
    b=b.replace("\n"," ")
    b=b.split(" ")
    print(len(b))
a=input("Enter a file with path in your PC:")
count_words(a)
print("*********")

## Write a Python program to remove newline characters from a file
def remove_line(filepath):
    a1 = open(filepath, "r+")
    b1 = a1.read()
    b1 = b1.replace("\n", " ")
    print("After removing the next line:",b1)
remove_line("Demo1.txt")
print("*********")

# Write a Python program to copy the contents of a file to another file
def copying_file(fromfilepath,tofilepath):
    with open(fromfilepath,"r") as f1, open(tofilepath,"w") as f2:
        for x in f1:
            f2.write(x)
    a=open("Demo1.txt")
    b=a.read()
    print("******files are copied*****")
    print("Data in copied file:\n",b)
copying_file("Demo1.txt","Demo2.txt")
print("***********")

#A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#".
#Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
#Example :
#If the file matter.txt has the following content stored in it :
#THE WORLD IS ROUND
def hash_code():
    a=open("matter.txt","r")
    b=a.read()
    for i in b:
        print(i,end="#")
hash_code()













