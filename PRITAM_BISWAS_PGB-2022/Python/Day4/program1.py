
"""
Write a simple program which loops over a list of user data (tuples containing a username, email and age)
and adds each user to a dictionary if the user is at least 16 years old. You do not need to store the age.
 Write a simple exception hierarchy which defines a different exception for each of these error conditions:
a. the username is not unique
b. the age is not a positive integer
c. the user is under 16
d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
e. Raise these exceptions in your program where appropriate. Whenever an exception occurs,
   your program should move onto the next set of data in the list. Print a different error message for each
   different kind of exception.
"""
# Exceptions
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
    ("pritam", "pritam@example.com", 21),
    ("astra", "astra@example", 19),
    ("diablo", "jane2@example.com", 25),
    ("steoamon", "steve@somewhere", 15),
    ("viper", "sage", 23),
    ("sage", "sage@example.com", -3),
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

        email_parts = email.split('@')
        if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
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

"""
Errors: 1.compile time 2.logical 3.run time

syntax errror eg.syntax missing or wrong in code
logical error eg. wrong output
run time(mistake is donw by user) eg.divide by zero

1.try: The try block lets you test a block of code for errors.
2.except: The except block lets you handle the error.
3.finally: The finally block lets you execute code, regardless of the result of the try- and except blocks.

syntax:
   
   try :
         statement (try a/b if it fails then it will go to exception )
   except Exception:
         statement (it will print exception message)
   finally:
         statement(it will be executed if we get error as well as if we don't get the error )
         

"""
