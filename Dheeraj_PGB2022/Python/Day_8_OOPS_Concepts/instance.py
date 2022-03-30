# 11. Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.

class Student:
	pass


class Marks:
	pass


s_obj = Student()
print(type(s_obj).__name__, isinstance(s_obj, Student))

m_obj = Marks()
print(isinstance(m_obj, object))