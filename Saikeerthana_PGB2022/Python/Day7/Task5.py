#Assign a different name to function and call it through the new name
	#Ex: Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
def fun_name(name,age):
    print("name is",name)
    print("age is",age)
new_func=fun_name
new_func("lucky",50)