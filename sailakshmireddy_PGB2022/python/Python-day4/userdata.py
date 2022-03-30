# Write a simple program which loops over a list of user data (tuples containing a username, email and age)
# and adds each user to a dictionary if the user is at least 16 years old. You do not need to store the age.
# Write a simple exception hierarchy which defines a different exception for each of these error conditions:
    #a. the username is not unique
	#b. the age is not a positive integer
	#c. the user is under 16
	#d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
	#e. Raise these exceptions in your program where appropriate. Whenever an exception occurs,
    # your program should move onto the next set of data in the list. Print a different error message for each different kind of exception.
userlist=[("user1","user1@gmail.com",18),("user2","user2@gmail.com",17),("user3","user3@gmail.com",16),("user4","user4@gmail.com",15),("user5","user5@gmail.com",18),("user5","user5@gmail.com",20),("user6","user6@gmail.com",-18)]

class Validated_username(Exception):
    pass
class Validate_email(Exception):
    pass
class Validate_age(Exception):
    pass
class Validate_positiveage(Exception):
    pass

dict={}

for user,mail,age in userlist:
    try:
        if user in dict:
            raise Validated_username
        if "@" not in mail:
            raise Validate_email
        if not age>0:
            raise Validate_positiveage
        if not (age>=16):
            raise Validate_age

    except Validated_username:
        print("{} already exits".format(user))
    except Validate_email:
        print("{}check your mail".format(mail))
    except Validate_age:
        print("{} is below 16years".format(user))
    except Validate_positiveage:
        print("for {} please give positive age".format(user))
    else:
        dict[user]=(user,mail,age)
for x,y,z in dict.values():
   print("{} your mail is {} and age is {}".format(x,y,z))

