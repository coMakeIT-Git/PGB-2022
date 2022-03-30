def calculate(a, b):
    return a+b, a-b

a, b = map(int, input("Enter two Numbers:").split())
add, sub = calculate(a,b)
print("Sum : ", add, "\nDifference: ", sub)
