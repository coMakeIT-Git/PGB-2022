"""  Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not."""
class Student:
    pass
class Marks:
    pass
obj1=Student()#creating instance
obj2=Marks()
print("checking whether the objects are instances of the said classes")
print(isinstance(obj1,Student))
print(isinstance(obj1,Marks))
print(isinstance(obj2,Student))
print(isinstance(obj2,Marks))
print("checking whether the said classes are subclasses of builtin object class")
print(issubclass(Student,object))
print(issubclass(Marks,object))
