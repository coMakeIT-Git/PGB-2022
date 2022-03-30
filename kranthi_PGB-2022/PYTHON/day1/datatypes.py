a = 5
b = 6.0
c = 3 + 5j
print(" a is of type:  ", type(a))
print("b is of type:  ", type(b))
print("c is of type:  ", type(c))
print('\n')
string = "This is a string "
string1 = ''' this 
is multiline
string'''
print(string, type(string))
print(string1, type(string1))

List=["Hi","I am","List"]
print(List,type(List))
print("\n")
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
print(Tuple1,type(Tuple1))
print(Tuple2,type(Tuple2))
print("\n")
print("True",type(True))
print("False",type(False))
print("\n")
set1 = set("This is a set")

print(set1,type(set1))

Dict={ 1: "dictionay", 2 : "is collection of ", 3:"key value"
}
Dict1={(1,"hello"),(2,"kranthi")}
print(Dict,type(dict))
print(Dict1)
print(Dict.get(2))
print("\n")
print("type casting string to int adding int and string")
g=20+int("201")#type casting string to int adding int and string
print(g)
print("type casting bool to string concating string and bool")
h="this is"+str(True)#type casting bool to string concating string and bool
print(h)
print("type casting tuple to list and concating list and tuple")
k = [1,2,3]+list((22,40))#type casting tuple to list and concating list and tuple
print(k)







