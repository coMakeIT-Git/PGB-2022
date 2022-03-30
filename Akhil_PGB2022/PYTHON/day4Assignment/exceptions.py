import re
#Insert data into dictionary
lst = [("adithya","ad342@mail.com",15),("mark","mark123@mail.com",17),("mark","suhas@mail.com",21),("ben","ben10@ymail.com",25),("arjun","arj342@mailcom",19)]
dc = {}
class nameError(Exception):
	pass
class ageError(Exception):
	pass
class emailError(Exception):
	pass
def validate(s):
	reg = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	if re.fullmatch(reg,s):
		return True
	else:
		return False

for i in lst:
	try:
		if i[0] in dc.keys():
			raise nameError("Name already exists")
		if i[2]<0 or i[2]<16:
			raise ageError("Invalid age")
		if not validate(i[1]):
			raise emailError("Invalid email")
		dc[i[0]] = i[1]	
	except nameError as ne:
		print(ne)
	except ageError as ae:
		print(ae)
	except emailError as exp:
		print(exp)
print(dc)


#Calculator
class formulaError(Exception):
	pass
	
def nums(a,b):
	try:
		return float(a),float(b)
	except:
		raise formulaError("Value Error")
print("Enter formula: ")
f = input()
while(f!="quit"):
	f = f.split()
	try:
		if len(f)!=3:
			raise formulaError("Invalid formula")
		if f[1]!='+' and f[1]!='-':
			raise formulaError("Invalid Operator")
		x,y = nums(f[0],f[2])
		if f[1]=='+':
			print(f"{x} + {y} = {x+y}")
		if f[1]=='-':
			print(f"{x} - {y} = {x+y}")
	except formulaError as e:
		print(e)
	print("Enter formula: ")
	f = input()



#Write a class to handle exceptions
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
            print(f"Error Message : {e}")
    def importerror(self):
        try:
            from pandas import notexistingmethod
        except ImportError as e:
            print(f"Error Message : {e}")
    def indexerror(self):
        a = "V"
        try:
            print(a[3])
        except IndexError as e:
            print(f"Error Message : {e}")
    def indentationerror(self):
        try:
            import indentError
        except IndentationError as e:
            print(f"Error Message : {e}")

    def valueerror(self):
        val="test"
        try:
            int(val)
        except ValueError as e:
            print(f"Error Message : {e}")
            
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


