#Define variables for each data type and store respective data
int=1
string="name"
boolean=True
float=10.23
list=[1,2,3]
tuple=("a","b","c")
set={1,2,"a"}
dict={"a":1,"b":2,"c":3}
print("##########")
#Try to modify the data and identify which data types are mutable and which are immutable
list=[1,2,3]
list[1]=5
print(list)
tuple=("a","b","c")
#tuple[0]="d" tuples are immutable
print(type(tuple))
print("##########")
# Create variables and assign multiple values and override the data types
list1=["a","b","c"]
list1=[1,2,3]
print(list1)
a="sai"
a="akash"
print(a)
print("##########")
#Define variable 'a' and store int and string types using + operator and resolve errors if any
a=32
b="b"
#print(a+b)=>TypeError: unsupported operand type(s) for +: 'int' and 'str'
#resolving
a="32"
b="b"
print(a+b)

#define variable 'b' and store string and boolean types using + operator and resolve errors if any
b="b"
c=True
#print(b+c)=>TypeError: can only concatenate str (not "bool") to str
#resolving
b="b"
c="True"
print(b+c)

#define variable 'c' and sote list and tuple types using + operator and resolve errors if any
c=[1,2,3]
d=(4,5,6)
#print(c+d)=TypeError: can only concatenate list (not "tuple") to list
#resolving
c=[1,2,3]
d=[(4,5,6)]
print(c+d)
print("##########")
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
#Add an element to the fruits list
fruits.append("mango")
print(fruits)
#Copy the fruits list
a=fruits.copy()
print(a)
#Return the number of times the value "cherry" appears in the fruits list
f=fruits.count("cherry")
print(f)
# Add the elements of cars to the fruits list
fruits.extend(cars)
print(fruits)
#What is the position of the value "cherry"
a=fruits.index("cherry")
print(a)
#Insert the value "orange" as the second element of the fruit list
fruits.insert(2,"orange")
print(fruits)
#Remove the second element of the fruit list
fruits.remove(fruits[2])
print(fruits)
#Remove the "banana" element of the fruit list
fruits.remove("banana")
print(fruits)
#Reverse the order of the fruit list
fruits.reverse()
print(fruits)
# Sort the cars list+
print("before sort:",cars)
cars.sort()
print("after sort:",cars)
# Remove all elements from the fruits list
fruits.clear()
print(fruits)
print("##########")
#Create a string
string="coMakeIT continuous innovation"
#Convert it into upper case
s=string.upper()
print(s)
#Convert into lower case
s=string.lower()
print(s)
#Return the number of times a specified value occurs in a string
s=string.count("a",0,9)
print(s)
#Return true if the string ends with the specified value
s=string.endswith("a",0,9)
print(s)
#Return True if all characters in the string are in the alphabet
s=string.isalpha()
print(s)
#Convert the first character of each word to upper case
s=string.title()
print(s)
#Convert the first character to upper case
s=string.capitalize()
print(s)
#Search the string for a specified value and returns the position of where it was found
s=string.index("e",0,15)
print(s)
#Reverse the string with slicing
s=string[::-1]
print(s)
print("##########")
#Create a tuple
tup=(1,2,3,3,"s","a")
#Return the number of times a specified value occurs in a tuple
t=tup.count(3)
print(t)
#Search the tuple for a specified value and returns the position of where it was found
t=tup.index("s",0,10)
print(t)
print("######")
#Create a dictionary with 3 different keys, all with the value '5' using inbuilt method
x = ("a","b","c")
y = 5
dict=dict.fromkeys(x, y)
print(dict)
#Create a dictionary
dict={"a":1,"b":2,"c":3}
#Return the value of the specified key
d=dict.get(b)
print(d)
#Print all key, value pairs
print(dict)
#Remove the element with the specified key
dict.pop("a")
print(dict)
#Remove the last inserted key-value pair
dict.popitem()
print(dict)
print("###########")
# Create a Set
set={"a","b",1,2,3}
#Add an element to the set
set.add(5)
print(set)
#Remove specific element
set.remove(3)
print(set)
print("#############")
#create 2 sets x and y and
x={1, 2, 3, 4, 5}
y={4,5,6,7,8}
#Return a set that contains the items that only exist in set x, and not in set y
print(x.difference(y))
#Remove the items that exist in both sets
x.difference_update(y)
print(x)
#Return True if no items in set x is present in set y
a=x.isdisjoint(y)
print(a)
#Return True if all items in set x are present in set y
a=x.issubset(y)
print(a)
#Return True if all items set y are present in set x
a=x.issuperset(y)
print(a)
#Return a set that contains all items from both sets, except items that are present in both sets
a=x.symmetric_difference(y)
print(a)
#Remove the items that are present in both sets, AND insert the items that is not present in both sets
x.symmetric_difference_update(y)
print(x)
print(y)
#Return a set that contains all items from both sets, duplicates are excluded
a=x.union(y)
print(a)
#Insert the items from set y into set x
x.update(y)
print(x)