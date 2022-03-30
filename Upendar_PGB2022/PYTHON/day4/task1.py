###########################################################
# 1  Write a simple program which loops over a list of user data (tuples containing a username, email and age) and adds each user to a dictionary if the user is at least 16 years old. You do not need to store the age.
# Write a simple exception hierarchy which defines a different exception for each of these error conditions:
# 	a. the username is not unique
# 	b. the age is not a positive integer
# 	c. the user is under 16
# 	d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
# 	e. Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move onto the next set of data in the list. Print a different error message for each different kind of exception.

import re
from random import randint

global regex
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

class NameNotUnique(Exception):
    pass
class NegativeAge(Exception):
    pass
class AgeNotSufficient(Exception):
    pass
class InvalidEmail(Exception):
    pass

class Student:
    def __init__(self, s_list):
        self.studentList = s_list
        self.student_db = {}
        self.add_to_db()

    def validate_name(self, username):
        if username in self.student_db:
            raise NameNotUnique("Username Already Exists")
        pass

    def validate_age(self, age):
        if 16 > age > 0:
            raise AgeNotSufficient("Age Is less than 16")
        if age < 0:
            raise NegativeAge("Age Is Less Than 0")

    def validate_email(self, email, username):
        if re.fullmatch(regex, email):
            pass
        else:
            raise InvalidEmail("Invalid Email Found")

    def add_to_db(self):
        for student in self.studentList:
            try:
                self.validate_name(student[0])

                self.validate_age(student[-1])

                self.validate_email(student[1], student[0])

                print(f"Student Added To DB : {student[0]}")
                self.student_db[student[0]] = student[1]

            except Exception as e:
                print(e)
test_cases = []

for i in range(10):
    age = randint(15, 22)
    test_cases.append((f"Student{i}", f"Student{i}@test.com", age))

test_cases.append(test_cases[-1])
test_cases.append(("Studentnegative", "Studentnegative@test.com", -10))
test_cases.append(("Studentemail", "Studentemail", 20))
test_cases.append(("Student1", "Studentemail1@test.com", 20))

print(test_cases)
s = Student(test_cases)

###########################################################

# 3 Write a Python program that takes a text file as input and returns the number of words of a given text file

def num_of_words(filepath):
    with open(filepath)as f:
        data=f.read()
        data.replace(","," ")
        return len(data.split(" "))
print(num_of_words("../data1"))

###########################################################
# 4 Write a Python program to remove newline characters from a file

def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(remove_newlines("data1"))
###########################################################
# 5 Write a Python program to copy the contents of a file to another file .
import shutil
shutil.copyfile('../data1', 'data')

#############################################################
# 6 Write a Python program that reads each row of a given csv file and skip the header of the file.
# Also print the number of rows and the field names.

import csv
def csv_file():
    csvfile = input("Enter CSV File: ")
    with open(csvfile, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        print(f"Total Number of Rows : {sum(1 for line in reader)}")
        print(f"field Names : {headers}")

csv_file()

#############################################################
# 7. A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#".
# 	Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
# 	Example :
# 	If the file matter.txt has the following content stored in it :
# 	THE WORLD IS ROUND

def insert_hash():
    with open("../matter", "r") as file:
        data = file.read()
        for char in data:
            print(char, end="#")
    print()
insert_hash()

#############################################################
# 8 Write a class to handle below exceptions
# 	a. ZeroDivisionError
# 	b. ImportError
# 	c. IndexError
# 	d. IndentationError
# 	e. ValueError
# 	f. Exception
# 	g. Raise any exception and handle it properly and use else,
# 	finally blocks to print something irrespective of exception

#class ZeroDivisionError(Exception):
    #pass
#class ImportError(Exception):
     #pass
#class IndexError(Exception):
     #pass
#class IndentationError(Exception):
     #pass
#class ValueError(Exception):
     #pass

#zero division error
try:
 a=10/0
 print(a)
except ZeroDivisionError:
    print("")
    print("Zero Division Exception Raised")
else:
    print("Success, no error")

#import error
try:
    import python
except ImportError:
    print("Import error is raised")
else:
    print("Success, no error")

#IndexError
try:
    a=[10,20,30]
    print(a[5])
except:
    print("IndexError is raised")
else:
    print("There is no error")

#Indentation error
try:
    for i in range(5):
      print(i)
except:
    print("Indentation error is raised")
else:
    print("There is no error")

#value error
try:
    import math
    math.sqrt(-10)
except:
    print("value error is raised")
else:
    print("No error")
finally:
    print("These are some exceptions in python")