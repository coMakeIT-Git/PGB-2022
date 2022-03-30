def calculation(x,y):
	add=x+y
	sub=x-y
	return add,sub
def show_employee(name,sal=9000):
	print("Employee name: ",name)
	print("Employee sal: ",sal)
def outer(a,b):
	def add():
		return a+b
	return add()+5
def recursive(x):
	if(x==0):
		return 0
	return x+recursive(x-1)
def display_student(name,age):
	print("Student name: ",name)
	print("Student age ",age)
def largest_element(l):
	m=l[0]
	for i in l:
		if m<i:
			m=i
	return m
#function calculation() such that it can accept two variables and returns addition and subtraction of that variables
print("addition and subtraction: ", calculation(10, 5))
#show_employee() will accept the employee’s name and salary and displays both If the salary is missing in the function call then assign default value 9000 to salary
show_employee("adithya")
#inner function to calculate the addition in the following way, outer function that will accept two parameters, a and b. outer function will add 5 into addition and return it
print("calculate addition using inner function: ", outer(10, 15))
#recursive function to calculate the sum of numbers from 0 to n
print("sum of 1-10 using recursive function:",recursive(10))
#Assigning a different name to function and call it through the new name
show_tudent=display_student
show_tudent("Adithya",21)
#largest item from a given list without using inbuilt methods
print("largest item in list:",largest_element([1,2,3]))
