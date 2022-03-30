#Write a program to create a function show_employee() using the following conditions.
	#a. It should accept the employee’s name and salary and display both.
	#b. If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name,sal=9000):
    print("empname:",name)
    print("emp sal:",sal)
show_employee("riya")
show_employee("reethu",300000)