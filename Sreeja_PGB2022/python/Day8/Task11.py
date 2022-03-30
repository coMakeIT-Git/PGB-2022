class name:
    pass
class age:
    pass
name1=name()
age1=age()
print("checking whether they are instances of the said classes or not")
print(isinstance(name1,name))
print(isinstance(name1,age))
print(isinstance(age1,age))
print(isinstance(age1,name))
print("checking whether the said classes are subclasses of the built-in object class or not")
print(issubclass(name,object))
print(issubclass(age,object))

