class Student:
    pass
class Marks:
    pass
stu = Student()
marks=Marks()
print("\n object 'stu' is an instance of Class Student:", isinstance(stu, Student))
print("\n object 'stu' is an instance of Class Object:", isinstance(stu, object))
print("\n object 'marks' is an instance of Class Marks:", isinstance(marks, Marks))
print("\n object 'marks' is an instance of Class Object:", isinstance(marks, object))
print("\n object 'marks' is an instance of Class Student:", isinstance(marks, Student))
print("\n object 'stu' is an instance of Class Marks:", isinstance(stu, Marks))