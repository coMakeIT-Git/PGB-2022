class Employee:
    def __init__(self, name, id, salary=9000):
        self.name = name
        self.id = id
        self.salary = salary

    def show_employee(self):
        print("\n Employee Name:", self.name, "\n Employee Id:", self.id, "\n Employee Salary:", self.salary)
e1 = Employee("Praphulla", "CMIT-1072")
print("Details of the employee:")
e1.show_employee()
e2 = Employee("Luna", "CMIT-1053", 10000)
e2.show_employee()
