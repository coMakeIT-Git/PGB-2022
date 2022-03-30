def function(n):
    for i in range(n,-1,-1):
        yield i
for int in function(4):
    print(int)

