def outer_fun(a,b):
    def addition(a,b):
        return a+b
    add = addition(a,b)
    return add+5
result = outer_fun(17,20)
print(result)
