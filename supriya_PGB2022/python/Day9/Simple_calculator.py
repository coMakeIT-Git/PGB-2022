#Design simple calculater application where user input is assumed to be a formula that consist of a number, an operator (at least + and -), 
# and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
#a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
#b.Try to convert the first and third input to a float(like so:float_value = float(str_value)). 
# Catch any ValueError that occurs, and instead raise a FormulaError
#c. If the second input is not '+' or '-', again raise a FormulaError
#d. If the input is valid, perform the calculation and print out the result. 
# The user is then prompted to provide new input, and so on, until the user enters quit.
import re
class FormulaErr(Exception): pass


def parse_input(usr_input):

  input_lst = usr_input.split()
  if len(input_lst) != 3:
    raise FormulaErr('Input does not consists of 3 elements')
  input1, operator, input2 = input_lst
  try:
    input1 = float(input1)
    input2 = float(input2)
  except ValueError:
    raise FormulaErr('The 1st and 3rd input values must be numbers')
  return input1, operator, input2

        

def Simple_calculator(input1, operator, input2):

  if operator == '+':
    return input1 + input2
  if operator == '-':
    return input1 - input2
  if operator == '*':
    return input1 * input2
  if operator == '/':
    return input1 / input2
  raise FormulaErr('{0} is not a valid operator'.format(operator))

            


while True:
  try:
    usr_input = input('>>> ')
  
        
    if input == 'quit':
      break
    input1, operator, input2 = parse_input(usr_input)
    res = Simple_calculator(input1, operator, input2)
    print(res)
  except Exception as e:
    print(e)