def add(a):
    if(a==0):
        return 0
    return a+add(a-1)
#calling the function with a different name
sum=add
print("\n The Sum is:", add(10))
print("\n The Sum is:", sum(6))