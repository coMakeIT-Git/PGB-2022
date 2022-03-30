import re
l=[("nithish","nithish11@gmail.com",21),("akhil","akhil1@gmail.com",15),("kranthi","kranthi21@gmail.com",20)]
d={}
class NameError(Exception):
    pass
class MailError(Exception):
    pass
class AgeError(Exception):
    pass

def valid(s):
    reg = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.fullmatch(reg, s):
        return True
    else:
        return False

for i in l:
    try:
        if i[0] in d.keys():
            raise NameError("Name exist")
        if i[2]<16:
            raise AgeError("Age less than 16")
        if not valid(i[1]):
            raise MailError("invalid mail id")

        d[i[0]]=i[1]
    except NameError as e:
        print(e)
    except AgeError as e2:
        print(e2)
    except MailError as e3:
        print(e3)

print(d)
