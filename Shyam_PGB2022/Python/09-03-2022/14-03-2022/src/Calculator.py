import re

class FormulaError(Exception):
    def __init__(self, msg):
        self.msg = msg


def test(inputx):
    regex = r'(\+|-)'
    l = inputx.split()
    try:
        if len(l) < 3:
            raise FormulaError("Less than 3")
        a, operator, b = l
        #print(a,b)

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise FormulaError("Float to str")
            #print("hello")

        if (not re.fullmatch(regex, l[1])):
            raise FormulaError("Error: Enter either + or - in the middle!")

        calculate(a, operator, b)
    except FormulaError as e:
        print(e.msg)

def calculate(a, operator, b):
    if operator == '+':
        print(a + b)
    elif operator == '-':
        print(a - b)


while True:
    print(' The format is [integer - operator -integer]')
    inputx = input("$ ")
    if inputx == 'quit':
        break
    test(inputx)
