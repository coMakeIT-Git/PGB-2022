#Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. 
# Also, it must return both addition and subtraction in a single return call.
def calculation(a,b):
    add=a+b
    sub=b-a
    return add,sub 
res=calculation(23,45)
print(res)
#Write a program to create a function show_employee() using the following conditions.
#It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(ename,salary):
    print(ename,salary)
show_employee(ename="Tom",salary=9000) 
#Create an inner function to calculate the addition in the following way    
#Create an outer function that will accept two parameters, a and b
#At last, an outer function will add 5 into addition and return it
def outer_func(c, d):
    def inner_func(c,d):
        return c+d
    sum= inner_func(c, d)
    return sum + 5
result = outer_func(15, 15)
print(result)
#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def rsum(n):
    if n <= 1:
        return n
    else:
        return n + rsum(n-1)

num = 10
total=rsum(num)
print("The sum is",total)
#Assign a different name to function and call it through the new name
#Ex: Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
def display_student(name, age):
    print(name,age)
   # print(age)
print_student=display_student
print_student("Supriya",20)



