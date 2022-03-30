from re import *

# 1. Write a simple program which loops over a list of user data (tuples containing a username, email and age) and adds each user to a dictionary if the user is at least 16 years old. You do not need to store the age. Write a simple exception hierarchy which defines a different exception for each of these error conditions:

# 	a. the username is not unique
# 	b. the age is not a positive integer
# 	c. the user is under 16
# 	d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
# 	e. Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move onto the next set of data in the list. Print a different error message for each different kind of exception.

class DuplicateUser(Exception):
    def __init__(self,val):
        self.val=val
    def __str__(self) -> str:
        return repr(self.val)


class ValidAge(Exception):
    def __init__(self,val):
        self.val=val
    def __str__(self) -> str:
        return repr(self.val)



class CheckAge(Exception):
    def __init__(self,val):
        self.val=val
    def __str__(self) -> str:
        return repr(self.val)

class EmailException(Exception):
    def __init__(self,val):
        self.val=val
    def __str__(self) -> str:
        return repr(self.val)

def check(email):
    #print(email)
    email_regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if fullmatch(email_regex,email):
        return True
    return False

a=[('manideep',12,'manideep.a@comakeit.com')
,('manohar',22,'manu@gmail.com'),
('manideep',31,'mani.a@comakeit.com'),
('fdhe',42,'fdhe.a@.com',
('fdhe',-12,'abc@gmail.com'))]
Users={}
for i in a:
    while 1:
        try:
            name,age,email=i[0],i[1],i[2]
            if name in Users:
                raise DuplicateUser(f"Already User exists with {name}")
            elif age<0:
                raise ValidAge(f"Age for {name} is negative")
            elif age<16:
                raise CheckAge(f"Age for {name} is less than 16")
            elif not check(email):
                raise EmailException(f"{email} isn't a valid email")
            else:
                Users[name]=email
        except DuplicateUser as e:
            print(e)
        except ValidAge as e:
            print(e)
        except CheckAge as e:
            print(e)
        except EmailException as e:
            print(e)
        finally:
            break
            
print(Users)

        
