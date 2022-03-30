#Task 1:
import re
class DuplicatUsernameError(Exception):
    pass
class UnderAgeError(Exception):
    pass
class InvalidEmailError(Exception):
    pass
class user():
    def __init__(self, username, email):
        self.username = username
        self.email = email
sample_list = [("Ram","ram12@gmail.com",25),
               ("Harish","harish34@gmail.com",29),
               ("Girish","girish56@gmail.com",15),
               ("John","john78@gmail.com",24),
               ("Harish","harish04@gmail.com",20),
               ("James","james78#$gmail.com",24)]
database = {}
for username, email, age in sample_list:
    try:
        if username in database:
            raise DuplicatUsernameError()
        if age < 16:
            raise UnderAgeError()
        if not(re.findall("@gmail.com$", email)):
            raise InvalidEmailError()
    except DuplicatUsernameError:
        print("The username '%s' is already present in the database" %username)
    except InvalidEmailError:
        print("'%s' is not a valid email id!!" %email)
    except UnderAgeError:
        print("'%s' User is underage"%age)
    else:
        database[username] = user(username,email)
print(database)

#Task 2:
class formulaError(Exception):
    pass
def nums(a, b):
    try:
        return float(a), float(b)
    except:
        raise formulaError("Value Error")
print("Enter formula(eg: 1 + 1): ")
f = input()
while (f != "quit"):
    f = f.split()
    try:
        if len(f) != 3:
            raise formulaError("Invalid formula")
        if f[1] != '+' and f[1] != '-':
            raise formulaError("Invalid Operator")
        x, y = nums(f[0], f[2])
        if f[1] == '+':
            print(f"{x} + {y} = {x + y}")
    except formulaError as e:
        print(e)
    print("Enter formula: ")
    f = input()

#Task 3:
file_name = input("Enter File name:")
num_of_words = 0
with open(file_name, 'r') as fn:
    for line in fn:
        words = line.split()
        num_of_words += len(words)
print("Number of words in '%s':"%file_name)
print(num_of_words)

#Task 4:
file_name1 = input("Enter file name:")
with open(file_name1, 'r') as newline_file:
    lines_with_newline = newline_file.readlines()
    print([a.rstrip('\n') for a in lines_with_newline])

#Task 5:
from os.path import exists as file_exists
src = input("Enter source file name: ")
dest = input("Enter destination file name: ")
if(file_exists(dest)):
    print("The file name already exists..Enter some other file name!!!")
    exit()
else:
    fileHandle = open(src, "r")
    text = fileHandle.readlines()
    fileHandle.close()
    fileHandle = open(dest, "w")
    for t in text:
        fileHandle.write(t)
    fileHandle.close()
    print("Contents of the file copied successfully")

#Task 6:
import csv
fields = []
rows = []
with open('students.csv', newline='') as csvfile:
    info = csv.reader(csvfile, delimiter = ' ', quotechar = ',')
    fields = next(info)
    for row in info:
        print(', '.join(row))
print("Total number of lines: %d"%(info.line_num))
print('Field names are:')
print(', '.join(field for field in fields))

#Task 7:
def hash_display():
    file1 = open("matter", "r")
    cont = file1.read()
    for letter in cont:
        print(letter, end = "#")
    file1.close()
hash_display()

#Task 8:
class NegativeError(Exception):
    pass
class Exception_handle:
    def __init__(self):
        self.zerodivisionerror()
        self.importerror()
        self.indexerror()
        self.indentationerror()
        self.valueerror()
        self.customexception()
    def zerodivisionerror(self):
        try:
            var=8.5/0
        except ZeroDivisionError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
    def importerror(self):
        try:
            from pandas import notexistingmethod
        except ImportError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
    def indexerror(self):
        a = "V"
        try:
            print(a[3])
        except IndexError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
    def indentationerror(self):
        try:
            import error
        except IndentationError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def valueerror(self):
        val="comakeit"
        try:
            int(val)
        except ValueError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
    def customexception(self):
        try:
            x = int(input("Enter a number between positive integer: "))
            if x < 0:
                raise NegativeError(x)
        except NegativeError as e:
            print("You provided {}. Please provide positive integer values only".format(e))
        finally:
            print("All Exceptions are handled:")
Exception_handle()



