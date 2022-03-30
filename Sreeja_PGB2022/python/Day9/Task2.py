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
                raise FormulaError("invalid operator")
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