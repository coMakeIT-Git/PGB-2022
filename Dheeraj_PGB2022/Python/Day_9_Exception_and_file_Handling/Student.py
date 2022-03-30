# 1. Write a simple program which loops over a list of user data (tuples containing a username, email and age) and adds each user to a dictionary if the user is at least 16 years old. You do not need to store the age. Write a simple exception hierarchy which defines a different exception for each of these error conditions:
#
# 	a. the username is not unique
# 	b. the age is not a positive integer
# 	c. the user is under 16
# 	d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
# 	e. Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move onto the next set of data in the list. Print a different error message for each different kind of exception.

from random import randint
import re

global regex

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

class DuplicateEmail(Exception):
    pass


class InvalidAge(Exception):
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

    def validate_name(self, uname):
        if uname in self.student_db:
            raise DuplicateEmail(f"DuplicateEmail Exception : Username Already Exists '{uname}'")
        pass


    def validate_age(self, age):
        if 16 > age > 0:
            raise AgeNotSufficient(f"AgeNotSufficient Exception : Underage '{age}'")
        if age < 0:
            raise InvalidAge(f"InvalidAge Exception : Age Not Valid '{age}'")

    def validate_email(self, email, uname):
        if re.fullmatch(regex, email):
            pass
        else:
            raise InvalidEmail(f"InvalidEmail Exception : Invalid Email Found '{email}'")

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

for i in range(30):
    age = randint(15, 22)
    test_cases.append((f"Student{i}", f"Student{i}@test.com", age))

test_cases.append(test_cases[-1])
test_cases.append(("Studentnegative", "Studentnegative@test.com", -10))
test_cases.append(("Studentemail", "Studentemail", 20))
test_cases.append(("Student1", "Studentemail1@test.com", 20))



# print(test_cases)
s = Student(test_cases)



