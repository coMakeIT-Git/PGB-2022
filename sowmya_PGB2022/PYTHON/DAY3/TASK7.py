class Student:
    pass #empty  class
class Marks:
    pass #empty class
student1 = Student() #object creation
marks1 = Marks() #object creation
print("check whether they are instances of the said classes or not.")
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object)) 