import re

#list of tuples containing valid and invalid data
data = [("HarveySpecter", "harveyspectergmail.com", 40), ("DonnaPaulsen", "DonnaPaulsen@gmail.com", 10), ("MikeRoss", "mikeross@gmail.com", 30), ("RachelZane", "rachelzane@gmail.com", 20), ("LouisLitt", "louislitt@gmail.com", 21),  ("MikeRoss", "mikeross@gmail.com", 30),  ("JessicaPearson", "jessicap@gmail.com", -56)]

class UniqueUserError(Exception):
    def __init__(self, msg, key):
        self.msg = msg
        print("\n User Name not unique at: ", key)

class InvalidAgeError(Exception):
    def __init__(self, msg, key, age):
        self.msg = msg
        print("\n Invalid Age at :", key, "  A:", age)

class UnderAgeError(Exception):
    def __init__(self, msg, key, age):
        self.msg = msg
        print("\n Invalid Age at :", key, "  A:", age)

class InvalidEmailError(Exception):
    def __init__(self, msg, key, email):
        self.msg = msg
        print("\n Invalid Email at - U:", key, "  E:", email)

def check(d, key):
    if key in d:
        return True
    else:
        return False

d =dict()
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
for e in data:
    try:
        if (check(d, e[0]) == True):
            raise UniqueUserError("\n Error: User Name must be unique!", e[0])
        if (e[2] <= 0):
            raise InvalidAgeError("\n Error: Enter a positive value for age!", e[0], e[2])
        if (not re.fullmatch(regex, e[1])):
            raise InvalidEmailError("\n Error: Enter a valid email address!", e[0], e[1])
        if (e[2] <= 16):
            raise UnderAgeError("\n Error: Age must be greater than 16!", e[0], e[2])
        elif e[2] > 16:
            d[e[0]] = e[1]

    except UniqueUserError as e:
        print(e.msg)
    except InvalidAgeError as e:
        print(e.msg)
    except UnderAgeError as e:
        print(e.msg)
    except InvalidEmailError as e:
        print(e.msg)


print("\n***Valid Data Inserted into Dictionary***\n", d)