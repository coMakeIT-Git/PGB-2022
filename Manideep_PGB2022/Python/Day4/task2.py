#  Design simple calculater application where user input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

# 	a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
# 	b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
# 	c. If the second input is not '+' or '-', again raise a FormulaError
# 	d. If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.
from re import *
class FormulaError(Exception):
    def __init__(self,val):
        self.val=val
    def __str__(self) -> str:
        return repr(self.val)



while 1:
    i=input("Enter Input\n")
    k=split(r'\s+',i)
    if len(k)!=3:
        raise FormulaError(f' {i} is not a valid input')
    else:
        try:
            a=float(k[0])
            b=float(k[2])
            OP="+-"
            if k[1] not in OP:
                raise FormulaError("Please check the Operator")
            if (k[1]=="+"):
                print(a+b)
            elif k[1]=='-':
                print(a-b)
        except FormulaError as e:
            print(e)
    print("Do u want to continue \n if Yes Enter 1 \n else Enter 0")
    y=int(input())
    if y==0:
        break