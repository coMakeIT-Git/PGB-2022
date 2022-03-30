msg="Good morning"
print(type(msg))
number=10
print(type(number))
pi=3.14
print(type(pi))
b=True
print(type(b))

li=["hi","hello","ram"]
print(li)
print(type(li))
li[1]="ravi"#mutabledatatype
print(li)
tp=("sam""keer","aish","vaish")
print(tp)
print(type(tp))
#tp[3]="sai"
#print(tp)#immutabldatatype
set={1,2,3,4}
print(set)
print(type(set))
set.add(5)#mutabledatatype
print(set)
room_num = {'john': 425, 'tom': 212,'rina':325}
print(room_num)
print(type(room_num))
room_num['john']=500#mutabledatatype
print(room_num)
#msg[1]="p"
#print(msg)
x=10
x=10.5
print("implict type conversion",x)
y=int(100.8)
print("explicit type conversion",y)
x=y=z=100
print(x)
print(y)
print(z)
a=10
h="python"
print("combined using int and str + operator",h+str(a))
b="java"
q=True
print("combined boolean and string using + operator",b+str(q))
c=["vedanth","vivek","sai",3.5]
r=("lucky","annie","riya")
print("combined list and tuple using + operator",c+list(r))
fruits = ['apple', 'banana', 'cherry']
f = input("Please enter a fruit name to add:\n")
fruits.append(f)
print("list after adding element",fruits)
mylist=fruits.copy()
print("copying elements of list",mylist)
print("REmoving all elements from fruits list",fruits.clear())
print("count of cherry",mylist.count("cherry"))
cars = ['Ford', 'BMW', 'Volvo']
newlist=mylist+(cars)
print("adding cars to list",newlist)
print("position of cherry ",mylist.index("cherry"))
mylist.insert(1, "orange")
print("adding orange at second position",mylist)
mylist.remove("banana")
print("removing banana element from list",mylist)
mylist.reverse()
print("reverse list",mylist)
cars.sort()
print("sort the cars list",cars)


