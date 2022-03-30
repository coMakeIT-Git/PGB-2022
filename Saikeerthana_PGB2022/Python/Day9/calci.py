"""  Design simple calculater application where user input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

	a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
	b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
	c. If the second input is not '+' or '-', again raise a FormulaError
	d. If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit."""
"""import re   
class FormulaError(Exception):
    pass
def parse_input(user_input):
    regex = r'(\+*-)'
    check = user_input.split()
    try:
        if len(check) < 3:
            raise FormulaError("Input does not exist 3 elements")
        n1, op, n2 = check

        try:
            n1 = float(n1)
            n2 = float(n2)
        except ValueError:
            raise FormulaError("Int to float conversion")


        if (not re.fullmatch(regex, check[1])):
            raise FormulaError("Only use '+' '-' operators .")
        calculate(n1, op, n2)
    except FormulaError as ex :
        print(ex)

def calculate(n1, op, n2):
  

  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2
  raise FormulaError('{0} is not a valid operator'.format(op))


while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  n1, op, n2 = parse_input(user_input)
  result = calculate(n1, op, n2)
  print(result)"""
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