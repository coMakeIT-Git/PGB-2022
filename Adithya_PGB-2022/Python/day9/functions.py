import re
#List of tuples to Dictionary
a=("adithya","adithya@gmail.com",14)
b=("balaji","balaji@gmailcom",14)
c=("adithya","akhil@gmail.com",14)
d=("Dheeraj","dheeraj",14)
dic={}
def func(a):
	regex = r'\b[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	if re.fullmatch(regex, a):
		return False
	else:
		return True
l=[a,b,c,d]
for i in l:
	try:
		if i[0] in dic.keys():
			raise Exception("name error")
		if i[2]<0 or i[2]>=16:
			raise Exception("age error")
		if(func(i[1])):
			raise Exception("email error")
		dic[i[0]]=i[1]
	except Exception as e:
		print(e)
print(dic)




#calculator to compute addition and subtraction operations
class FormuleError(ValueError):
	pass
def calculator(i):
	try:
		l=i.split()
		if(len(l)!=3):
			raise FormuleError("Lenght is not 3")
	except FormuleError as fe:
		print(fe)
	regn="[0-9]+"
	regc="[+-]"
	try:
		a=float(l[0])
		b=float(l[2])
	except ValueError:
		print(FormuleError)
	try:
		if not re.fullmatch(regc,l[1]):
			raise FormuleError("expected character is not defined")
	except FormuleError as fe:
		print(fe)
	if(l[1]=='+'):
		return a+b
	if(l[1]=='-'):
		return a-b
	else:
		return ""
while(True):
	i=input()
	if(i=="exit"):
		break
	print(calculator(i))

