"""  Write a Python program to crate two empty classes,
 Student and Marks. Now create some instances and check whether
 they are instances of the said classes or not.
Also, check whether the said classes are subclasses
 of the built-in object class or not."""

class student:
    pass
class marks:
    pass

stu1=student()
mark=marks()


print("Tells wether stu1 is a instance of student or not :")

print(isinstance(stu1,student))

print("Tells wether mark is a instance of marks class or not :")

print(isinstance(mark,marks))

print("Tells wether stu1 is a instance of marks or not :")

print(isinstance(stu1,marks))

print("student is a subclass of object or not:")
print(issubclass(student,object))

print("marks is a subclass of object or not:")
print(issubclass(marks,object))