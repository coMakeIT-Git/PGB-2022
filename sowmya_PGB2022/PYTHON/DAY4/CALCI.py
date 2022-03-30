import re

class FormulaError(Exception):
    pass
# using Regular Expressions
def check(user_input):
    regex = r'(\+|-)'
    li = user_input.split()
    try:
        if len(li) < 3:
            raise FormulaError(" elements are  less than 3")
        n1, op, n2 = li

        try:
            n1 = float(n1)
            n2 = float(n2)
        except ValueError:
            raise FormulaError(" invalid conversion:Float to str")


        if (not re.fullmatch(regex, li[1])):
            raise FormulaError("use '+' '-' operators ")
        calculate(n1, op, n2)
    except FormulaError as ex:
        print(ex)

def calculate(n1, op, n2):
    if op=='+':
        print(n1 + n2)
    if op=='-':
        print(n1 - n2)

while True:
    user_input = input()
    if user_input == 'quit':
        break
    check(user_input) 