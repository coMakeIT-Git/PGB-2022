import math

class UserDefinedException(Exception):
    def __init__(self, msg):
        self.msg = msg

try:
    try:
        #ZeroDivisionError
        '''a = 1 / 0'''

        #IndentationError
        '''if(3>2):
        return True'''

        #ImportError
        '''import numpy'''

        #IndexError
        '''a = [1,2,3]
        print(a[4])'''

        #ValueError
        '''print(math.sqrt(-1))'''

        #Exception not listed
        a = 100 / "10"


    except ZeroDivisionError as e:
        raise UserDefinedException("Error: Division by zero is undefined!") from e

    except IndentationError as e:
        raise UserDefinedException("Error: Improper Indentation") from e

    except ImportError as e:
        raise UserDefinedException("Error: Package not found") from e

    except IndexError as e:
        raise UserDefinedException("Error: Index out of bounds") from e

    except ValueError as e:
        raise UserDefinedException("Error: Invalid Value") from e

    except Exception as e:
        raise UserDefinedException("Error: Unknown Exception") from e


except UserDefinedException as err:
    print(err.msg)
