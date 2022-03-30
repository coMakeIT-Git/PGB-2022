#a program to create function calculation() such that it can accept two variables 
# calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

def function(a,b):
    return a+b,a-b


k= function(8,10)

print("Sum is {} , Difference is {}".format(k[0],k[1]))

#a program to create a function show_employee()
#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name,salary=9000):
    print('Employee Name is {} \n Employee salary is {}'.format(name,salary))
    
show_employee('Likhitha')
show_employee('Likhitha',20000)


#Create an outer function that will accept two parameters, a and b
def outer(a,b):
    def inner(a,b):
        return a+b
    return 5+inner(a,b)

j=outer(9,6)
print("Outer function is ",j)


#program to create a recursive function to calculate the sum of numbers from 0 to 10
def recursion(a):
    if(a<=1):
        return a  
    else:
        return a+recursion(a-1)
    
print("Sum of 10 numbers using recursion: ",recursion(10))

#different name to function and call it through the new name
def display_student(name,age):
    print("Student name is {}, age is {}".format(name,age))
    
show_student=display_student
show_student("Likhitha",20)


#Find the largest item from a given list without using inbuilt methods
def largest(l):
    r=l[0]
    for i in l:
        if i>r:
            r=i
    return r

print(largest([9,89,76,65,45,98,96]))
      
      



    