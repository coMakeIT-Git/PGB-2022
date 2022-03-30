#import sys
class CustomException(Exception):
    pass
class Exceptions():
    def CheckforZDE():
        try:
            a = int(input())
            b = int(input())
            c = a/b
            if b == 0:
                raise ZeroDivisionError
            else:
                print(c)
        except ZeroDivisionError as e:
            print("Argument2 can't be zero")
        finally:
            print('This is always executed')

    def ValueError():
        try:
            amount = 1999
            if amount < 2999:
                raise ValueError("Account balance is low")
            else:
                print("Can proceed to payment")
        except ValueError as e:
            print(e)


    def IndentationError():
        try:
            '''
            def f():
            ip = ['praph', 'g']
            for i in ip:
            if i == 'g':
            '''
        except IndentationError as e:
            print(e)

    def IndexError():
        try:
            list = [1, 2, 6, 7, 10, 6]
            print(list[5])
        except IndexError as e:
            print("\n Index Error:", e)

    def ImportError():
        try:
            print(sys.version)
        except ImportError as e:
            print(e)

    def CustomException():
        try:
            num = int(input("Enter a number: "))
            if num < 50:
                raise CustomException
            elif num > 50:
                raise CustomException
        except CustomException:
            print("This is Custom Exception")


while True:
    print("\nMAIN MENU")
    print("1. ZeroDivisionError")
    print("2. ValueError")
    print("3. IndentationError")
    print("4. IndexError")
    print("5. ImportError")
    print("6. CustomException")
    print("5. Exit")
    choice = int(input("Enter the Choice"))
    if choice == 1:
        Exceptions.CheckforZDE()
    if choice == 2:
        Exceptions.ValueError()
    if choice == 3:
        Exceptions.IndentationError()
    if choice == 4:
        Exceptions.IndexError()
    if choice == 5:
        Exceptions.ImportError()
    if choice == 6:
        Exceptions.CustomException()
    elif choice == 7:
        break