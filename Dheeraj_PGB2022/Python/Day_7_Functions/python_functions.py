class PythonFunctions:
    def __init__(self):

        self.calculation(5, 10)

        print("Using default value : ")
        self.show_employee("Dheeraj")
        print("Using parameter value")
        self.show_employee("Dheeraj", 20000)

        print(f"Sum (Using inner and outer) = {self.outer_func(3, 17)}")

        print(f"Sum (Recursive) = {self.recursive_add(10)}")

        student_details = self.print_student
        print("Calling Using New Function Name : ")
        student_details("Dheeraj", 21)

        print(f"Max Element = {self.find_max([81, 7, 199, 1, 4, 6, 11, ])}")

    # Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
    def calculation(self, a, b):
        print("Given Numbers \na = {}\nb = {}".format(a, b))
        print(f"Addition = {a+b}, Subtraction = {a-b}")
        return a + b, a - b

    # Write a program to create a function show_employee() using the following conditions.
    # 	a. It should accept the employee’s name and salary and display both.
    # 	b. If the salary is missing in the function call then assign default value 9000 to salary
    def show_employee(self, name, salary=9000):
        print("Name : {}\nSalary : {}".format(name, salary))

    # Create an inner function to calculate the addition in the following way
    # 	a. Create an outer function that will accept two parameters, a and b
    # 	b. Create an inner function inside an outer function that will calculate the addition of a and b
    # 	c. At last, an outer function will add 5 into addition and return it
    def outer_func(self, a, b):
        def add():
            return a + b
        return add() + 5

    # Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
    def recursive_add(self, s):
        if s == 1:
            return 1
        return s + self.recursive_add(s - 1)

    # Assign a different name to function and call it through the new name
    def print_student(self, name, age):
        print(f"Name : {name}, Age : {age}")
        return name, age

    # Find the largest item from a given list without using inbuilt methods
    def find_max(self, lst):
        m = lst[0]
        for i in lst[1:]:
            if m < i:
                m = i
        return m


run = PythonFunctions()
