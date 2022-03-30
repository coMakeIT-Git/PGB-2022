import re

# 3. Write a Python program that takes a text file as input and returns the number of words of a given text file.
# 	Note: Some words can be separated by a comma with no space.

def num_of_words():
    with open("matter.txt", "r") as file:
        data = file.read()
        print("Total Number of Words in File :", len(re.findall(r"[\w']+", data)))

num_of_words()

# 4. Write a Python program to remove newline characters from a file

def remove_newline():
    with open("matter.txt", "r+") as file:
        data = file.read()
        file.seek(0)
        data = data.replace('\n', ' ')
        file.write(data)

remove_newline()

# 5. Write a Python program to copy the contents of a file to another file .

from os import path

def copy_file():
    ifile = input("Enter Source File Name : ")
    if not path.exists(ifile):
        print("Input file Does Not Exists")
        return copy_file()

    ofile = input("Enter Destination File Name : ")
    if path.exists(ofile):
        print("Output File Already Exists")
        return copy_file()

    if ofile == "":
        ofile = "(copy)" + ifile

    with open(ifile, "r") as infile:
        data = infile.read()
    with open(ofile, "w+") as outfile:
        outfile.write(data)

copy_file()

# 6. Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.

import csv

def csv_file():
    csvfile = input("Enter CSV File Name (csvfile.csv) : ")
    with open(csvfile, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        print(f"Total Number of Rows : {sum(1 for line in reader)}")
        print(f"feild Names : {headers}")

csv_file()

# 7. A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#".
# 	Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
# 	Example :
# 	If the file matter.txt has the following content stored in it :
# 	THE WORLD IS ROUND

def insert_hash():
    with open("matter.txt","r") as file:
        data = file.read()
        for char in data:
            print(char, end="#")
    print()

insert_hash()

# 8. Write a class to handle below exceptions
# 	a. ZeroDivisionError
# 	b. ImportError
# 	c. IndexError
# 	d. IndentationError
# 	e. ValueError
# 	f. Exception
# 	g. Raise any exception and handle it properly and use else, finally blocks to print something irrespective of exception

class CustomException(Exception):
    pass

class ExceptionHandling:
    def __init__(self):
        self.ZeroDivisionError_Handler()
        self.ImportError_Handler()
        self.IndexError_Handler()
        self.IndentationError_Handler()
        self.ValueError_Handler()
        self.CustomException_Handler()
        self.else_finally_Handler()

    def ZeroDivisionError_Handler(self):
        try:
            a = 1 / 0
        except ZeroDivisionError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def ImportError_Handler(self):
        try:
            from re import notexistingmethod
        except ImportError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def IndexError_Handler(self):
        l = ["a"]
        try:
            print(l[3])
        except IndexError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def IndentationError_Handler(self):
        try:
            import importerror

        except IndentationError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def ValueError_Handler(self):
        valerr = input("Enter String : ")
        try:
            int(valerr)
        except ValueError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def validate(self, t):
        if t < 20:
            raise CustomException("This is an custom Exception")

    def CustomException_Handler(self):
        test = 16
        try:
            self.validate(test)
        except CustomException as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def else_finally_Handler(self):
        for i in range(5, 0, -1):
            try:
                a = int(input("Enter 1st Number : "))
                b = int(input("Enter 2nd Number : "))
                output = a // b
            except Exception as e:
                print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
            else:
                print(f"Output is : {output}")
            finally:
                print(f"{i-1} Chances Left")

ExceptionHandling()
