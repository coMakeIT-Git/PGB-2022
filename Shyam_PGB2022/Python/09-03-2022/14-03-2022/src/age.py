class UserNameNotUnique(Exception):
    pass


class AgeNotPositive(Exception):
    pass


class AgeUnder16(Exception):
    pass


class CheckEmailId(Exception):
    pass


class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age


listNeed = [
    ("TonyStark", "shyamdoggaoff@gmail.com", 21),
    ("TonyStark", "tonystark@example", 7),
    ("StephenStrange", "stepherstrange@gmail.com", 15),
]

dicti = {}

for username, email, age in listNeed:
    try:
        if username in dicti:
            raise UserNameNotUnique()
        if age < 0:
            raise AgeNotPositive()
        if age < 16:
            raise AgeUnder16()

        email_parts = email.split('@')
        if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
            raise CheckEmailId()

    except UserNameNotUnique:
        print("Name: %s already existed in database" % username)
    except AgeNotPositive:
        print("Age not valid: %d" % age)
    except AgeUnder16:
        print("User age %s is valid." % username)
    except CheckEmailId:
        print("'%s' is not valid" % email)

    else:
        dicti[username] = User(username, email, age)
