#simple program which loops over a list of user data (tuples containing a username, email and age) 
# and adds each user to a dictionary if the user is at least 16 years old. You do not need to store the age. 
# Write a simple exception hierarchy which defines a different exception for each of these error conditions:

	#a. the username is not unique
	#b. the age is not a positive integer
	#c. the user is under 16
	#d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
	#e. Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move onto the next set of data in the list. Print a different error message for each different kind of exception.

import re
class DuplicateUsernameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class UnderageError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

# A class for a user's data

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

example_list = [
    ("ram", "ram@example.com", 21),
    ("bro", "bro@example", 19),
    ("jane", "jane2@example.com", 25),
    ("steve", "steve@somewhere", 15),
    ("joe", "joe", 23),
    ("anna", "anna@example.com", -3),
]

directory = {}

for username, email, age in example_list:
    try:
        if username in directory:
            raise DuplicateUsernameError()
        if age < 0:
            raise InvalidAgeError()
        if age < 16:
            raise UnderageError()
        
        regex = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"

        #email_parts = email.split('@')
        #if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
        
        #using regex expression for validating email
        if re.fullmatch(regex,email):
            print("Email is correct")
            
        else:
            raise InvalidEmailError()

    except DuplicateUsernameError:
        print("Username '%s' is in use." % username)
    except InvalidAgeError:
        print("Invalid age: %d" % age)
    except UnderageError:
        print("User %s is underage." % username)
    except InvalidEmailError:
        print("'%s' is not a valid email address." % email)

    else:
        directory[username] = User(username, email)
