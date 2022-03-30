def Sum(n):
    if(n==0):
        return 0
    return n + Sum(n-1)

print("Sum: ", Sum(10))