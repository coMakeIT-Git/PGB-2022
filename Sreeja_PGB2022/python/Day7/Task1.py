print("adding and subtracting two numbers and returning  them")

def addsub(n1,n2):
    add=n1+n2
    sub=n1-n2
    return add,sub
print(addsub(50,25))

print("creating the employ function and giving default value to salary")
def show_employ(name,salary=9000):
    print("employ name:",name)
    print("salary:",salary)
show_employ("raju",100000)
show_employ("sreeja")

print("creating and outer function and creating function inside the outer function and performing addition")
def outer(a,b):
    def inner(a,b):
        return a+b
    result=inner(a,b)
    return result+5
print(outer(10,20))
    
