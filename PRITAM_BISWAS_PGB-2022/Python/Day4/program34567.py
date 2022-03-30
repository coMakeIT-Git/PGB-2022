# file exception handling
"""
3. Write a Python program that takes a text file as input and returns the number of words of a given text file.
Note: Some words can be separated by a comma with no space.
"""
def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("file.txt"))

"""
4. Write a Python program to remove newline characters from a file (multiple blank lines)
"""
with open("file.txt") as f:
    print ("".join(line for line in f if not line.isspace()))

"""
5. Write a Python program to copy the contents of a file to another file .( if file already exits then raise a exception and use input from user to create a new file with new name)
"""
# open both files
with open('file.txt', 'r') as firstfile, open('newfile.txt', 'a') as secondfile:
    # read content from first file
    for line in firstfile:
        # append content to second file
        secondfile.write(line)


"""
6. Write a Python program that reads each row of a given csv file and skip the header of the file. 
Also print the number of rows and the field names.()
"""
import csv
fields = []
rows = []
with open('stroke_data.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar=',')
 # Following command skips the first row of the CSV file.
 fields = next(data)
 for row in data:
   print(', '.join(row))
print("\nTotal no. of rows: %d"%(data.line_num))
print('Field names are:')
print(', '.join(field for field in fields))

"""
7. A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#". 
	Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
	Example :
	If the file matter.txt has the following content stored in it :
	THE WORLD IS ROUND
"""
def insert_hash():
    with open("matter.txt","r") as file:
        data = file.read()
        for char in data:
            print(char, end="#")
    print()

insert_hash()

