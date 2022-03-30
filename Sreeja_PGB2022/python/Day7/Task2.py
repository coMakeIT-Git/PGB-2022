print("Python program to print sum of first 10 natural numbers using recursive function")
def recursion_sum(n):
   if n <= 1:
       return n
   else:
       return n + recursion_sum(n-1)

print("Sum is: ",recursion_sum(10))

print("creating new name to existing function")
def old_fun(name,age):
    print(name,age)
new_fun=old_fun
new_fun("sreeja",20)

print("printing the largest item fropm the list")
l=["1","2","3","4"]
max=l[0]
for i in range(1,len(l)):
    if(l[i]>max):
        max=l[i]
print(max)

print("Convert string into a datetime object")