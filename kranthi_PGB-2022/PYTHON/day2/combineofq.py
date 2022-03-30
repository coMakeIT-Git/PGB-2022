#a program to create function calculation() such that it can accept two variables and calculate addition and subtraction

a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("Program to print sum and difference in  a single call:")
def addsub(a,b):
    s=a+b
    d=a-b
    return (s,d)
print(addsub(a,b))

#employee program for default salary
def show_employee(c,d=9000):
    print("Employee name:",c)
    print("salary is :",d)
print("function to print default 9000 salary when salary was not given:")
print(show_employee('Ravi'))
print(show_employee('kranthi',12000))


#Inner and outer function
print("Inner and outer function to print sum+5:")
def outer(k,m):
    def addition(q,r):
        return q+r
    sum1=addition(k,m)
    return sum1+5
print(outer(9,11))



#Recurssive funtion to print sum of 0 to 10 nubers
print("Recurssive funtion to print sum of 0 to 10 nubers")
def recur(n):
    if(n<=1):
        return n
    else:
        return n+recur(n-1)
print(recur(10))



#Assign a different name to function and call it through the new name

print("Assign a different name to function and call it through the new name")
def display_student(name,age):
    print("Student name is:",name)
    print("Student age  is:", age)

show_student = display_student
print(show_student('Mahesh',21))




#the largest item from a given list without using inbuilt methods
print("the largest item from a given list without using inbuilt methods:")
def large(l):
    max=-9999
    a=len(l) #caluclates the length of list
    for i in range(a):
        if(l[i]>max):
            max=l[i]
    return max
myl=[1,9,11,34,50,4,5]
print(large(myl))


#program to use for loop to print the following reverse number pattern
print("program to use for loop to print the following reverse number pattern")
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

#Count all letters, digits, and special symbols from a given string
str1="Hikranthi@##$2001"
a=len(str1)
c=0
c1=0
c2=0
for i in range(a):
    if(str1[i].isalpha()):
        c = c+1
    elif(str1[i].isdigit()):
        c1=c1+1
    else:
        c2=c2+1
print("Count all letters, digits, and special symbols from a given string")
print("Number of alphabets = ",c)
print("Number of digits = ",c1)
print("Number of symbols = ",c2)




