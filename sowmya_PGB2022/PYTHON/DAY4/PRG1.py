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