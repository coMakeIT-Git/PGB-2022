#Write a class to handle below exceptions
	#a. ZeroDivisionError
	#b. ImportError
	#c. IndexError
	#d. IndentationError
	#e. ValueError
	#f. Exception
	#g. Raise any exception and handle it properly and use else, finally blocks to print something irrespective of exception

class CustomException(Exception):
    pass

class Exception_handling:
    def __init__(self):
        self.ZeroDivision_handler()
        self.Import_handler()
        self.Index_handler()
        self.Indentation_handler()
        self.Value_handler()
        self.Custom_exception_handler()
        self.else_finally_Handler()

    def ZeroDivision_handler(self):
        try:
            a=10/0
        except ZeroDivisionError as zde:
            print("Error is:",zde)

    def Import_handler(self):
        try:
            import notexistingmethod
        except ImportError as ie:
            print("Error is:",ie)

    def Index_handler(self):
        l = ["a"]
        try:
            print(l[3])
        except IndexError as e:
            print("Error is:",e)

    def Indentation_handler(self):
        try:
            print("IndentationError")
        except IndentationError as IE:
            print("Error is:",IE)

    def Value_handler(self):
        value = input("Enter String:")
        try:
            int(value)
        except ValueError as ve:
            print("Error is:",ve)

    def validate(self, t):
        if t < 20:
            raise CustomException("This is an custom Exception")

    def Custom_exception_handler(self):
        test = 16
        try:
            self.validate(test)
        except CustomException as e:
            print("Error name is:",e)

    def else_finally_Handler(self):
        for i in range(2, 0, -1):
            try:
                a = int(input("Enter 1st Number : "))
                b = int(input("Enter 2nd Number : "))
                output = a // b
            except Exception as e:
                print("Error Name:".e)
            else:
                print("Output is :",output)
            finally:
                print((i-1),"Chances Left")
Exception_handling()

