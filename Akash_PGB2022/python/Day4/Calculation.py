
# Design simple calculater application where user input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

	#a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
	#b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
	#c. If the second input is not '+' or '-', again raise a FormulaError


class Calculation_Error(Exception):
    pass

def user_data(user_input):
    user_input = user_input.split(" ")
    try:
        if len(user_input)!=3:
            raise Calculation_Error("Length of the input must be 3")
        num1,operator,num2=user_input

        num1=float(num1)
        num2=float(num2)
    except ValueError:
        raise Calculation_Error("The input must be digits only")
    return num1,operator,num2
def Calculation(num1,operator,num2):
    if operator=="+":
        return num1+num2
    if operator=="-":
        return num1-num2
    else:
        raise Calculation_Error("please enter a '+' or '-' operator only")

while True:
    user_input=input("Enter a values using space: ")
    if user_input=="quit":
        break
    num1, operator, num2=user_data(user_input)
    result=Calculation(num1,operator,num2)
    print(result)

