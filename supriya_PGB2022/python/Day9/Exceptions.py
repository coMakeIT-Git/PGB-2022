# Write a simple program which loops over a list of user data (tuples containing a username, email and age) and adds each user to a dictionary
#  if the user is at least 16 years old. You do not need to store the age. 
# Write a simple exception hierarchy which defines a different exception for each of these error conditions:
#a. the username is not unique
#b. the age is not a positive integer
#c. the user is under 16
#d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
#e. Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move onto the next set of data in the list. 
#Print a different error message for each different kind of exception
import re
class NotUniqueUsernameErr(Exception):
    pass

class InvalidAgeErr(Exception):
    pass

class UnderageErr(Exception):
    pass

class InvalidEmailErr(Exception):
    pass

# A class for a user's data

class Student:
    def __init__(self, username, emailadd,age):
        self.username = username
        self.emailadd = emailadd
        self.age=age
        
Student_list = [
    ("tom", "tom@gmail.com", 17),
    ("jerry", "jerry@gmail.com", 20),
    ("tom","abc@gmail.com",18),
    ("Mr.Beam", "beam@gmail", 25),
    ("micky", "micky@example", -18),
    ("teddy", "tedd", 23),
    
]

dict = {}

for username, emailadd, age in Student_list:
    try:
        if username in dict:
            raise NotUniqueUsernameErr()
        if age < 0:
            raise InvalidAgeErr()
        if age < 16:
            raise UnderageErr()
        
    except NotUniqueUsernameErr:
        print("Username '%s' exists." % username)
    except InvalidAgeErr:
        print("Invalid age: %d" % age)
    except UnderageErr:
        print("Student %s is underage." % username)
    except InvalidEmailErr:
        print("'%s' is invalid email address." % emailadd)
    
    else:
        dict[username] = emailadd
        #print(dict)
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    if(re.search(regex,emailadd)):   
          print("Valid Email")   
    else:   
          print("Invalid Email")
        
            


       
  
