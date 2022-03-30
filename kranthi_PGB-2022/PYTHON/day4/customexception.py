'''
 Write a class to handle below exceptions
	a. ZeroDivisionError
	b. ImportError
	c. IndexError
	d. IndentationError
	e. ValueError
	f. Exception
	g. Raise any exception and handle it properly and use else, finally blocks to print something irrespective of exception

'''

class CustomException(Exception):
    pass

class ExceptionHandling:
    def __init__(self):
        self.ZeroDivisionError_Handler()
        self.ImportError_Handler()
        self.IndexError_Handler()

        self.ValueError_Handler()
        self.CustomException_Handler()
        self.else_finally_Handler()

    def ZeroDivisionError_Handler(self):
        try:
            a = 1 / 0
        except ZeroDivisionError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def ImportError_Handler(self):
        try:
            from re import notexistingmethod
        except ImportError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def IndexError_Handler(self):
        l = ["a"]
        try:
            print(l[3])
        except IndexError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")



    def ValueError_Handler(self):
        valerr = input("Enter String : ")
        try:
            int(valerr)
        except ValueError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def validate(self, t):
        if t < 20:
            raise CustomException("This is an custom Exception")

    def CustomException_Handler(self):
        test = 16
        try:
            self.validate(test)
        except CustomException as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def else_finally_Handler(self):
        for i in range(1, 0, -1):
            try:
                a = int(input("Enter 1st Number : "))
                b = int(input("Enter 2nd Number : "))
                output = a // b
            except Exception as e:
                print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
            else:
                print(f"Output is : {output}")
            finally:
                print(f"{i-1} Chances Left")

ExceptionHandling()