class Student:
    pass

class Marks:
    pass

s = Student()
m = Marks()

print("s is an instance of Student: ", isinstance(s, Student))
print("s is an instance of Marks: ", isinstance(s, Marks))
print("\nm is an instance of Marks: ", isinstance(m, Marks))
print("m is an instance of Student: ", isinstance(m, Student))
print("\ns is an instance of Object: ", isinstance(s, object))
print("m is an instance of Object: ", isinstance(m, object))

