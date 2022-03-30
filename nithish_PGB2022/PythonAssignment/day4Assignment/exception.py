
def hash_display():
    f=open("matter.txt",'r')
    data=f.read()
    for letter in data:
        print(letter,end="#")

print("Hash Display:")
hash_display()

#---------------------------------------------------------------------------------

class NegativeError(Exception):
    pass

class Exception_handle:
    def __init__(self):
        self.zerodivisionerror()
        self.importerror()
        self.indexerror()
        self.indentationerror()
        self.valueerror()
        self.customexception()
    def zerodivisionerror(self):
        try:
            var=8.5/0
        except ZeroDivisionError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
    def importerror(self):
        try:
            from pandas import notexistingmethod
        except ImportError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
    def indexerror(self):
        a = "V"
        try:
            print(a[3])
        except IndexError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
    def indentationerror(self):
        try:
            import error
        except IndentationError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def valueerror(self):
        val="comakeit"
        try:
            int(val)
        except ValueError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
    def customexception(self):
        try:
            x = int(input("Enter a number between positive integer: "))
            if x < 0:
                raise NegativeError(x)
        except NegativeError as e:
            print("You provided {}. Please provide positive integer values only".format(e))
        finally:
            print("All Exceptions are handled:")

Exception_handle()

