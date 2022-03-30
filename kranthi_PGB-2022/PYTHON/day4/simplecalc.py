class FormulaError(Exception):pass

def parse_input(ur_input):
    input_list=ur_input.split()
    if (len(input_list)!=3):
        raise FormulaError('please enter only 3 separated values')
    n1,op,n2=input_list
    try:
        n1=float(n1)
        n2=float(n2)
    except ValueError:
        raise FormulaError('first and third values should be numbers')
    return n1,op,n2
def caluclate(n1,op,n2):
    if op=='+':
        return n1+n2
    elif op=='-':
        return n1-n2
    elif op=='*':
        return n1*n2
    elif op=='/':
        return n1/n1
    else:
        raise FormulaError('{} it is not a valid operater',format(op))


while True:
    ur_input=input('Enter space separated formula:')
    if ur_input=='quit':
        break
    n1,op,n2=parse_input(ur_input)
    result=caluclate(n1,op,n2)
    print(result)