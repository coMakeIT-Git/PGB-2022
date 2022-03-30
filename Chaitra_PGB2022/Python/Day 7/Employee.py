def show_employee(Name, Salary="9000"):
    print("\nName: ", Name, "\nSalary: ", Salary)

Name = input("Enter Name: ")
Salary = input("Enter Salary: ")
if(Salary == ""):
    show_employee(Name)
else:
    show_employee(Name, Salary)