import re

class FormulaError(Exception):
    def __init__(self, msg):
        self.msg = msg
# using Regular Expressions
def test(inputx):
    regex = r'(\+|-)'
    l = inputx.split()
    try:
        if len(l) < 3:
            raise FormulaError("Error: Arguments are Less than 3")
        a, operator, b = l

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise FormulaError("Error: Float to str")


        if (not re.fullmatch(regex, l[1])):
            raise FormulaError("Error: Only use '+' '-' operators for computation .")
        calculate(a, operator, b)
    except FormulaError as e:
        print(e.msg)

def calculate(a, operator, b):
    if operator == '+':
        print(a + b)
    elif operator == '-':
        print(a - b)

while True:
    print('Enter expression in the given format is a  op  b')
    inputx = input("$ ")
    if inputx == 'quit':
        break
    test(inputx)