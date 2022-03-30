""" Write a simple program which loops over a list of user data (tuples containing a username, email and age) and adds each user to a dictionary if the user is at least 16 years old. You do not need to store the age. Write a simple exception hierarchy which defines a different exception for each of these error conditions:

	a. the username is not unique
	b. the age is not a positive integer
	c. the user is under 16
	d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
	e. Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move onto the next set of data in the list. Print a different error message for each different kind of exception."""
import re   

class notunique(Exception):
    pass
class agenegative(Exception):
    pass
class underage(Exception):
    pass
class invalidemail(Exception):
    pass
class user:
    def __init__(self,name,mail,age):
        self.name=name
        self.mail=mail
        self.age=age
li=[("sam", "sam@example.com", 21),
    ("bob", "bob@example", 19),
    ("sam", "sam2@example.com", 25),
    ("ravi", "ravi@somewhere", 15),
    ("reethu", "reethu", 23),
    ("riya", "riya@example.com", -3)]
result={}
for name,mail,age in li:
    try:
        if name in li:
            raise notunique()
        if age<0:
            raise agenegative()
        if age<16:
            raise underage()
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, mail):
            print("valid mail")
        else:
            raise invalidemail
    except notunique:
        print("Username '%s' is in use." % name)
    except agenegative :
        print("Invalid age: %d" % age)
    except underage:
        print("User %s is underage." % name)
    except invalidemail:
        print("'%s' is not a valid email address." % mail)
    else:
        result[name] = user(name, mail,age)
    finally:
        print("Executed")

