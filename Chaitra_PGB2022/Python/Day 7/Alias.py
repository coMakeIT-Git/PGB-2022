def Sum(n):
    if(n==0):
        return 0
    return n + Sum(n-1)

SumOf10 = Sum
print("Sum: ", SumOf10(10))