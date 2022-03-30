
#simple calculater application where user input 
# is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, 
# separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

	#a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
	#b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
	#c. If the second input is not '+' or '-', again raise a FormulaError
	#d. If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

class FormulaError(Exception): 
    pass


def parse_input(user_input):

  input_list = user_input.split()
  if len(input_list) != 3:
    raise FormulaError('Input does not consist of three elements')
  n1, op, n2 = input_list
  try:
    n1 = float(n1)
    n2 = float(n2)
  except ValueError:
    raise FormulaError('The first and third input value must be numbers')
  return n1, op, n2


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
  print(result)
