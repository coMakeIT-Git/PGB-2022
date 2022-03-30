a=10,20,30,'hello',50,30,'hello',30
print("Tuple:",type(a))

b=a.count(30)
print("30 is present",b,"number of times in tuple")

c=a.index('hello')
print("hello is present at index pos",c)

u=('k1','k2','k3')
v=5
thisdict=dict.fromkeys(u,v)
print("a dictionary with 3 different keys, all with the value '5' using inbuilt method :", thisdict)

dict={1: "Hello", 2:'Python',3 : 7}

print("Dictionary Created",dict)

x=dict.get(3)
print("Value present at key3",x)

del dict[2]
print("Removing 2nd key in dictionary",dict)


d=dict.popitem()
print("Removed last inserted element",dict)

set1={'mango','apples','cars','buses'}
set1.add(23)

print("Element is added in set",set1)

set1.remove('buses')
print("Element is removed in set",set1)

setx={'a','b','c',1,2,3}
sety={1,2,3,'x','y','z'}

onlysetx=setx-sety
print("Elements only present in setx:",onlysetx)

comm=setx&sety
setx=[ele for ele in setx if ele not in comm]
sety=[ele for ele in sety if ele not in comm]

print("Removed the items that are common in both sets",setx,sety)

print("Checking elements present in 2 sets are equal or not:",setx==sety)

seta={1,2,3,6}
setb={1,2,3,7,9,6}

print("Return True if all items in set x are present in set y: ",setx<=sety)

print("Return True if all items in set y are present in set x:", sety<=setx)

uni=seta|setb
inter=seta&setb

print("Return a set that contains all items from both sets, except items that are present in both sets: ",uni-inter)


print("Return a set that contains all items from both sets, duplicates are excluded: ",uni)

o={9,0,8}
p={5,6,7}

o.update(p)
print(o)

