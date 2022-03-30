''' Write a simple program which loops over a list of user data (tuples containing a username, email and age)
and adds each user to a dictionary if the user is at least 16 years old. You do not need to store the age.
Write a simple exception hierarchy which defines a different exception for each of these error conditions:

	a. the username is not unique
	b. the age is not a positive integer
	c. the user is under 16
	d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
	e. Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should
	move onto the next set of data in the list. Print a different error message for each different kind of exception.'''

import re
from random import randint
global regex

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

class MyError(Exception):
    pass
class UniqueName(Exception):
    pass
class AgeNotSufficient(Exception):
    pass
class InvalidAge(Exception):
    pass
class CheckMail(Exception):
    pass



class Student:
    def __init__(self, s_list):
        self.studentList = s_list
        self.student_dict = {}
        self.add_to_dict()
    def validate_name(self,usr_name):
        if usr_name in self.student_dict:
            raise UniqueName("Not Unique Name Exception The name already exists")
        pass
    def validate_age(self,age):
        if 16>age>0:
            raise AgeNotSufficient("AgeNotSufficient Exception: you are underaged")
        elif age<0:
            raise InvalidAge("Invalidage Exception: please enter valid age")

    def validate_mail(self,mail):
        if re.fullmatch(regex,mail):
            pass
        else:
            raise CheckMail("InvalidMail exception: your mail is not proper")
    def add_to_dict(self):
        for s in self.studentList:
            try:
                self.validate_name(s[0])
                self.validate_mail(s[1])
                self.validate_age(s[-1])
                print("Student added sucessfully")
                self.student_dict[s[0]]=s[1]
            except Exception as e:
                print(e)

print("All exceptions regarding student info:")
my_sl=[]
for i in range(15):
    age= randint(15,21)
    my_sl.append((f"Student{i}",f"student{i}@test.com",age))
my_sl.append(("Studentnegative", "Studentnegative@test.com", -10))
my_sl.append(("Studentemail", "Studentemail", 20))
my_sl.append(("Student1", "Studentemail1@test.com", 20))

s=Student(my_sl)





