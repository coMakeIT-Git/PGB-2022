
#Write a program to create function calculation()
def calculation(a,b):
    s=a+b
    sub=a-b
    return("sum is {}\nand\nsub is {}".format(s,sub))
a=calculation(3,5)
print(a)
print("#############")

#Write a program to create a function show_employee()
def show_employee(name,salary=9000):
    return ("Employee name is {}\nEmployee salary is {}".format(name,salary))
s=show_employee("sai")
print("default args:",s)
s=show_employee("sai",25000)
print("with args:",s)
print("###########")

#Create an outer function that will accept two parameters, a and b
def outer(a,b):
    def inner(a,b):
        return (a+b)
    i= inner(a,b)
    return(i+5)
a= outer(2,3)
print("sum of num using inner and outer:",a)
print("##########")

#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def add(a):
    if a:
        return a+add(a-1)
    else:
        return 0
a=add(10)
print("sum of numbers from 0 to 10 is: ",a)
print("#########")

#Assign a different name to function and call it through the new name
def display_student(name,age):
    print("name is {},age is {}".format(name,age))
show_student=display_student
show_student("reddy",24)
print("#########")

#Find the largest item from a given list without using inbuilt methods
a=[1,6,9,15,22,8,5,11]
b=0
for x in a:
    if x>b:
        b=x
    else:
        b=b
print("largest num in list is: ",b)


