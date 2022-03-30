a=10
print("data type for a",type(a)) 

b=9.3
print("data type for b",type(b))

c=True
print(type(c))

string1="Python"
print("String data type :",string1)

d="5"
e=int(d)
print(a+e,"Typecasting")

h=str(a)
print("Integer & String com",string1+h)


list1=[10, 20, 'hello',69]
print("List :",list1)

e=('Ram',56,89,'hello')
print("Tuple :",e)

f={2.5,"Sets",(1,2,3)}
print("Set :",f)

g=10+b
print("Combined 2 data types using +",g)

list2=[8.9,"lkj",98]
print("Combined list1 and list2:",list1+list2)

fruits = ['apple', 'banana', 'cherry']
storefruits=fruits.copy()

print("Copied",storefruits)

cars = ['Ford', 'BMW', 'Volvo']
fruits.append('Grapes')
print("Added one element in fruits:",fruits)

fruits.clear()
print("Removed all elements in fruits",fruits)

count1=storefruits.count('cherry')
print("cherry appeared",count1,"number of times")

finallist=storefruits+cars
print("Cars list is added to fruits list",finallist)

indexpos=finallist.index('cherry')
print("Position of cherry in list",indexpos)

finallist.insert(2,'Orange')
print("Orange is added at 2nd position in list",finallist)

finallist.pop(2)
print("Element is removed at 2nd index position",finallist)

storefruits.remove('banana')
print("Banana is removed",storefruits)

storefruits.reverse()
print(storefruits)

cars.sort()
print("Cars are sorted",cars)

