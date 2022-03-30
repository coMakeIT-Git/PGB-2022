import re

#list of tuples containing valid and invalid data
data = [("HarryPotter", "harry@gmail.com", 20), ("LunaLovegood", "luna@gmail.com", 10), ("HarryPotter", "harry@gmail.com", 20), ("TeddyBear", "teddy@yahoo.com", 20), ("HermioneGranger", "hermione@hotmail.com", 21), ("GinnyWeasley", "ginny@gmail.com", 0), ("RonWeasley", "ron@gmail.com", -4), ("RemusLupin", "remusgmail.com", 30)]
print("***Tuples of data***")
print(data)

class UniqueUserError(Exception):
    def __init__(self, msg, key):
        self.msg = msg
        print("\nUser Name not unique at: ", key)

class InvalidAgeError(Exception):
    def __init__(self, msg, key, age):
        self.msg = msg
        print("\nInvalid Age at - U:", key, "  A:", age)

class UnderAgeError(Exception):
    def __init__(self, msg, key, age):
        self.msg = msg
        print("\nInvalid Age at - U:", key, "  A:", age)

class InvalidEmailError(Exception):
    def __init__(self, msg, key, email):
        self.msg = msg
        print("\nInvalid Email at - U:", key, "  E:", email)

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
            raise UniqueUserError("Error: User Name must be unique!" , e[0])
        if (e[2] <= 0):
            raise InvalidAgeError("Error: Enter a positive value for age!", e[0], e[2])
        if (not re.fullmatch(regex, e[1])):
            raise InvalidEmailError("Error: Enter a valid email address!", e[0], e[1])
        if (e[2] <= 16):
            raise UnderAgeError("Error: Age must be greater than 16!", e[0], e[2])
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