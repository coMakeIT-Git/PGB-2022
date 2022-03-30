#2. Design simple calculater application where user input is assumed to be a formula that consist of a number,
# an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(),
# and check whether the resulting list is valid:
	#a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
	#b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
	#c. If the second input is not '+' or '-', again raise a FormulaError
	#d. If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

class FormulaError(Exception):
    pass

def user_data(user_input):
    user_input = user_input.split(" ")
    try:
        if len(user_input)!=3:
            raise FormulaError("length of input must be 3")
        a,b,c=user_input

        a=float(a)
        c=float(c)
    except ValueError:
        raise FormulaError("the input must be digits only")
    return a,b,c

def Calculation(a,b,c):
    if b=="+":
        return a+c
    if b=="-":
        return a-c
    else:
        raise FormulaError("please enter a '+' or '-' operator only")

while True:
    user_input=input("Enter a values using space: ")
    if user_input.lower()=="quit":
        break
    a,b,c=user_data(user_input)
    result=Calculation(a,b,c)
    print(result)














