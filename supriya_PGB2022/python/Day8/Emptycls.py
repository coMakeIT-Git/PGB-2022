#Write a Python program to crate two empty classes, Student and Marks. 
# Now create some instances and check whether they are instances of the said classes or not. 
# Also, check whether the said classes are subclasses of the built-in object class or not.
class Professor:
    pass 
class Student:
    pass 
teaching = Professor()
learning = Student()
print(isinstance(teaching, Professor))
print(isinstance(learning, Professor))
print(isinstance(learning, Student)) 
print(isinstance(learning, Student))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Professor, object))
print(issubclass(Student, object)) 
