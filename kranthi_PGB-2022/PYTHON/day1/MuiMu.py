l=[1,3,5]
print(l)
print("id of the first list",id(l))
print(type(l))
l[0]=8
print(l)
print("id of the updated list",id(l))
print(type(l))
print("both list are having same id hence Lists are mutable")
print("similarly sets and dictionaries are also mutable")
print("\n")
age=21
print(age)
print("id of first created age",id(age))
print(type(age))

age=22
print(age)
print("id of second created age",id(age))

print("Here age is pointing to different id upon changing henc int is immutable")
print("booleans, floats, complex numbers are also immutable")
print("\n")
tuple1 = (0, 1, 2, 3)
print("Tuple is immutable so we get below error")


message = "This is a message"
print("message is immutable so we get below error")
tuple1[0] = 4

print(tuple1)
message[0] = 'p'
print(message)