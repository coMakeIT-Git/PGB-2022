import re


class DuplicateUserName(Exception):
    pass
class InvalidAgeNumber(Exception):
    pass
class UnderAgeNumber(Exception):
    pass
class InvalidEmail(Exception):
    pass
class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
list1=[("Balaji","Balaji123@gmail.com",21),
       ("Akhil","akhil@123",13),
       ("Nithish","nithish@123",-8),
       ("adithya","adithya@123",24)]
dictionary={}
def email_check(email):
    regexp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regexp,email):
        return True
    else:
        return False
for username,email,age in list1:
    try:
        if username in dictionary:
            raise DuplicateUserName
        if age<0:
            raise InvalidAgeNumber
        if age<16:
            raise UnderAgeNumber
        if(not(email_check(email))):
            raise InvalidEmail
    except DuplicateUserName:
        print("Username is in use")
    except InvalidAgeNumber:
        print("Invalid age number")
    except UnderAgeNumber:
        print("User is underage")
    except InvalidEmail:
        print("Email is not valid")
    else:
        dictionary[username]=User(username,email)
for key,value in dictionary.items():
    print(key,value.username,value.email)

#classes to handle below exceptions
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

