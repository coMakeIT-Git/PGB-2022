def Add(a, b):
    def Calculate(a,b):
        return a+b
    s = Calculate(a,b)
    return s+5

a, b = map(int, input("Enter two Numbers:").split())
res = Add(a,b)
print("Sum : ", res)
