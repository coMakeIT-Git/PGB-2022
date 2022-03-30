def calculation(var1,var2):
    add=var1+var2
    sub=var1-var2
    return add,sub
print("Enter two integer values to get addition and subtraction:")
var1=int(input("Enter first value:"))
var2=int(input("Enter second value:"))
addition,subtraction=calculation(var1,var2) #calling calculation function
print("Addition of two numbers is:",addition)
print("Subtraction of two numbers is:",subtraction)

#Creating Function Employee
def showEmployee(empname,empsalary=9000): #Assigning default salary value
    print("Employee name is:",empname)
    print("Employee salary is:",empsalary)
empname=input("Enter employee name:")
empsalary=int(input("Enter salary:"))
showEmployee(empname,empsalary)
showEmployee(empname) # Takes employeesalary has default value

#Calculation using Inner Function
def outer_function(var1,var2):
    def inner_function():
        add=var1+var2
        return add

    add=inner_function() #Calling inner function
    add=add+5
    return add
var1=int(input("Enter first value:"))
var2=int(input("Enter second value:"))
print(outer_function(var1,var2))

#Recursive function for sum 0 to 10
def recursive_addition(num):
    if num:
        return(num+recursive_addition(num-1))
    else:
        return 0
sum=recursive_addition(10)
print("Sum of the numbers from 0 to 10 is:",sum)

#Assign a different name to function and call it through the new name
def display_student(name,age):
    print("Name of the student is:",name)
    print("age of the student is:",age)
display_student("shashi",21)
show_student=display_student
show_student("shashi",21) # calling same function but with assigning a different name

list=[10,8,18,43,6,34,5,14,3]
max1=0
for i in range(0, len(list)):
    if(list[i]>max1):
        max1=list[i]
print("Maximum value from the list is:",max1)
#print(max(list)) #using inbuilt method
