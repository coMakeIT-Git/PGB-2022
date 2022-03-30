#Write a Python program that takes a text file as input and returns the number of words of a given text file.
#Note: Some words can be separated by a comma with no space.
def numof_words(filepath):
   with open(filepath) as f:
       txt = f.read()
       txt.replace(",", " ")
       return len(txt.split(" "))
f = open("Day9/sample.txt", "r")
print(numof_words("Day9/sample.txt"))

#Write a Python program to remove newline characters from a file
def Remove_Newlinechar(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]
print(Remove_Newlinechar("Day9/sample.txt"))

#Write a Python program to copy the contents of a file to another file .
import os.path
print(os.getcwd())
if  os.path.isfile('Day9/copy.txt'):
    print ("Already exists")
else:
    print("valid")
    f1 = open("Day9/sample.txt", "r")
    f2 = open("Day9/copy.txt", "w")
    for line in f1:
      f2.write(line)

#Write a Python program that reads each row of a given csv file and skip the header of the file. 
#Also print the number of rows and the field names.    
import csv
fields = []
rows = []
with open('Day9/username.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar=',')
 # Following command skips the first row of the CSV file.
 fields = next(data)
 for row in data:
   print(', '.join(row))
print("\nTotal no. of rows: %d"%(data.line_num))
print('Field names are:')
print(', '.join(field for field in fields))

# A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#". 
#Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
#Example :If the file matter.txt has the following content stored in it :
#THE WORLD IS ROUND
def hash_display():
    file = open("Day9/matter.txt","r")
    data = file.read()
    for letter in data:
        print(letter, end="#")

    file.close()

hash_display()
