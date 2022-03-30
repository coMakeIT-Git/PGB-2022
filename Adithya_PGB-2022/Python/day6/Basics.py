def f(s):
	for i in s:
		if not i.isalpha():
			return False
	return True
#Defining variables for each data type and storing respective data
print("Different datatypes in python",end="\n\n")
a=5
b="adithya"
c=5.2
d=True
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print()
print("overriding the variables",end="\n\n")
a="abc"
print("a is overriding from integer to string ",a)
a=[1,2,3]
print("a is overriding from string to list ",a)
a=(1,2,3)
print("a is overriding from list to tuple ",a)
a={1:'a',2:'b'}
print("a is overriding from tuple to Dictionary ",a)
print(end="\n")

print("mutable and immutable datatypes ",end="\n\n")
l=[1,2,3]
print("address of list before ",id(l))
l.append(4)
print("address of list after",id(l))
print("As address of list doesn't change on list Operations, list is mutable ")
print(end="\n")
l=(1,2,3)
print("address of tuple before ",id(l))
l=(4,5,6)
print("address of tuple after ",id(l))
print("As address of tuple changed on tuple Operations, tuple is immutable ")
print(end="\n")
l={1:'a',2:'b'}
print("address of Dictionary before ",id(l))
l[3]='c'
print("address of Dictionary after ",id(l))
print("As address of Dictionary doesn't change on Dictionary Operations, Dictionary is mutable ")
print(end="\n")
l={1,2}
print("address of set before",id(l))
l.add(3)
print("address of set after ",id(l))
print("As address of set doesn't change on set Operations, set is mutable ")
print(end="\n\n")
print("Adding different datatypes")
print(end="\n")
#Defining variable 'a' and storing int and string types using + operator and resolving errors 
try:
	a=7+'a'
except:
	print("String and Integer cannot be added")
#defining variable 'b' and storing string and boolean types using + operator and resolving errors
try:
	b="String"+True
except:
	print("string and boolean cannot be added")
#defining variable 'c' and storing list and tuple types using + operator and resolving errors
try:
	c=[1,2,3]+(1,2,3)
except:
	print("List and Tuple cannot be added")
print()
print("List Operations",end="\n\n")
#creating fruits and car list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
#appending new element
fruits.append('pineapple')
print("fruit list after adding new element: ",fruits)
#creating new copy of fruits
new=fruits.copy()
print("New copy of fruits list: ",new)
#fruits.clear() to remove all the elements from fruit
print("cherry count in fruits list: ",fruits.count('cherry'))
#Adding the elements of cars to the fruits list
fruits.extend(cars)
print("car elements added to fruits list: ",fruits)
print("index of cherry in fruits: ",fruits.index('cherry'))
#Inserting the value "orange" as the second element(index=1) of the fruit list
fruits.insert(1,"orange")
print("Fruits list after inserting oranges at first index: ",fruits)
fruits.remove(fruits[1])
print("Fruits list after removing element at position 1 ",fruits)
fruits.remove("banana")
print("Fruits list after removing banana ",fruits)
fruits.reverse()
print("Fruits list after reversing ",fruits)
cars.sort()
print("Cars list after sorting ",cars)

print()
print("String Operations",end="\n\n")
s="ravi teja"
s=s.upper()
print("String after converting it into uppercase ",s)
s=s.lower()
print("String after converting it into lowercase ",s)
print("Count of character a in String is ",s.count("a"))
print("String ends with a: ",s.endswith("a"))
print("All characters in String are alphabets ",f(s))
sl=s.split()
for i in range(len(sl)):
	sl[i]=sl[i][0].upper()+sl[i][1:]
print("Words in String Starts with uppercase",sl)
s=s[0].upper()+s[1:]
print("String first character changed to uppercase ",s)
print("Index of a in String",s.index("a"))
s=s[::-1]
print("reversing the string using slicing",s)
print()
print("Tuple Operations",end="\n\n")
tu=("amar","akbar","antony")
print("Tuple: ",tu)
print("Count of amar in tuple: ",tu.count("amar"))
print("Index of Akbar in tuple: ",tu.index("akbar"))
print()
print("Dictionary Operations",end="\n\n")
d=dict()
t1=("apple","banana","mango")
t2=(5)
d=dict.fromkeys(t1,t2)
print("Dictionary created using tuples",d)
print("Retriving value of key apple: ",d.get("apple"))
for key,value in d.items():
	print("Key And Value in Dictionary ",key,value)
d.pop("apple")
print("Dictionary after poping apple key ",d)
d.popitem()
print("Dictionary after poping last key ",d)
print()
print("Set Operations",end="\n\n")
s={1,2,3}
s.add(4)
print("Set after adding a element",s)
s.remove(1)
print("Set after removing element",s)
x={1,2,3}
y={1,4,5}
ns=x-y
print("Set that consists only elements of x but not in y ",ns)
common=x.intersection(y)
x=x-common
y=y-common
print("Sets after removing common elements of both ",x,y)
print("Return True if no items in set x is present in set y: ",x.isdisjoint(y))
print("Return True if all items in set x are present in set y:", x.issubset(y))
print("Return True if all items in set y are present in set x:", x.issuperset(y))
print("Return a set that contains all items from both sets, except items that are present in both sets: ",x.symmetric_difference(y))
print("Remove the items that are present in both sets, AND insert the items that is not present in both sets: ",x.symmetric_difference_update(y))
print("Return a set that contains all items from both sets, duplicates are excluded: ",x.union(y))
y.update(x)
print("Insert the items from set y into set x:",y)