class Student:
    pass
class Marks:
    pass
s = Student()
m = Marks()
print(isinstance(s, Student))
print(isinstance(m, Student))
print(isinstance(s, Marks))
print(isinstance(m, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))