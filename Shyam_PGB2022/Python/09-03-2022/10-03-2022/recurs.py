def add(x):
    if x:
        return x+add(x-1)
    else:
        return 0
res = add(10)
print(res)