import re


class FormulaError(Exception):
    pass
def number_check(num):
    exp="[0-9]+"
    if re.fullmatch(exp,num):
        return True
    else:
        return False
def operator_check(op):
    exp="[+-]"
    if re.fullmatch(exp,op):
        return True
    else:
        return False
def calculate(string):
    s=string.split()
    if(len(s)!=3):
        raise FormulaError("Input does not consists of three elements.")
    n1,op,n2=s
    if(not(number_check(n1))):
        return "Invalid Input"
    if (not (number_check(n2))):
        return "Invalid Input"
    if (not (operator_check(op))):
        return "Invalid Input"
    try:
        n1=float(n1)
        n2=float(n2)
    except ValueError:
        raise FormulaError("The first and third input must only contain the numbers.")
    if op=='+':
        return n1+n2
    if op=='-':
        return n1-n2
    else:
        raise FormulaError("It is not a valid operator.")

while(True):
    string = input("Enter string value:")
    if(string=="quit"):
        break
    print(calculate(string))


