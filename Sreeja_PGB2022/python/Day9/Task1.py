import re   

class duplicatename(Exception):
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
li=[("ravi", "mailto:ravi@example.com", 24),
    ("ram", "ram@example", 11),
    ("lakshmi", "mailto:lakshmi@example.com", 95),
    ("rakesh", "rakesh@somewhere", 19),
    ("sita", "sita", 23),
    ("riya", "mailto:riya@example.com", -3)]
result={}
for name,mail,age in li:
    try:
        if name in li:
            raise duplicatename()
        if age<0:
            raise agenegative()
        if age<16:
            raise underage()
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, mail):
            print("valid mail")
        else:
            raise invalidemail
    except duplicatename:
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
        print("It always executes")

