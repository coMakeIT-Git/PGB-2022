class FormulaError(Exception):
    pass

def check(str):
    l=str.split()
    if(len(l)!=3):
        raise FormulaError("Pass only 3 elements")
    try:
        a=float(l[0])
        b=float(l[2])
    except ValueError:
        raise FormulaError("first and third value error")
    return a,b,l[1]

def calculate(a,b,op):
    if(op=='+'):
        print("sum =",a+b)

    elif(op=='-'):
        print("subtraction =",a-b)
    else:
        raise FormulaError("Not a valid operator")

while(True):
    str=input("Enter operation: ")
    if(str=="quit"):
        break
    a,b,op=check(str)
    result=calculate(a,b,op)
