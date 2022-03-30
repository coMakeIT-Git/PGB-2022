from typing import List

x = "Arjun"
y = 12.34
p = True
q = 45
b = 'A'

dct = {1:"A",2:"B",3:"C"}
print(dct)
dct[2] = "G"
print(dct)
print("Dictionary is mutable")
lst = [3,4,5,6,8]
print(lst)
lst.remove(5)
print(lst)
print("List is mutable")
st = {3,4,5,6,8}
print(st)
st.add(2)
print(st)
print("Set is mutable")
s = "malli"
print("Address of s:",id(s))
s = s+"karjun"
print("Address of s:",id(s))
print()
#Assign multiple values and override the data types
var = 3
print("Var value: ",var,"Var Type:",type(var))
var = "War"
print("Var value: ",var,"Var Type:",type(var))
var = False
print("Var value: ",var,"Var Type:",type(var))
var = 3.088
print("Var value: ",var,"Var Type:",type(var))
var = []
print("Var value: ",var,"Var Type:",type(var))
var = {}
print("Var value: ",var,"Var Type:",type(var))
var = ()
print("Var value: ",var,"Var Type:",type(var))
print()
#Concatenating different data types
try:
	a = 5+"Vinay"
except:
	print("String cannot be added to int")
try:
	a = "coMaKeIT"+True
except:
	print("String cannot be added to boolean")
try:
	a = []+()
except:
	print("list cannot be added to tuple")
print()
#####################################################################

#6


fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

print(fruits)

fruits = ['apple', 'banana', 'cherry']

print(f'Current Fruits List {fruits}')

f = input("Please enter a fruit name:\n")
fruits.append(f)

print(f'Updated Fruits List {fruits}')
fruit = fruits.copy()
fruits.clear()

count = fruit.count("cherry")
print(count)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

cherry = fruit.index("cherry")

print(cherry)

fruits.insert(1, "orange")

print(fruits)

fruit.pop(1)

# displaying list after removing

print(fruits)

fruits.remove("banana")
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)
####################################################

#7



string = "Welcome to python"

# convert string to uppercase
print(string.upper())

print(string.lower())

print(string.count("0"))

print(string.endswith('o'))

print(string.title())

print(string.capitalize())

print(string.isalpha())

print(string.find('o'))

print(string[:: -1])

###################################################################

#tuple


tp = (4,5,6,87,8,5,12)
print("Tuple:" , tp)
print("Return the number of times a '5' occurs in a tuple: ",tp.count(5))
print("Search the tuple for '87' and return the position: ",tp.index(87))

t = (3,4,7,12)
print()
print("Dictionary")

#Dictionary


print("Creating dictionary using a tuple and value:",dict.fromkeys(t,5))
d = dict(zip(t,tp))
print("Creating dictionary using 2 tuples:",d)
print("Getting the value using key '7':",d.get(7))
print("Printing key value pairs:")
for k,v in d.items():
	print("key:",k,"value:",v)
print("Remove the element with key '4':",d.pop(4))
print("Remove the last inserted key-value pair",d.popitem())
print()


#######################################################################


t = {3,5,6,8,2,0,1}
print("Set: ",st)
print("Adding elements to set: ",st.add(23))
print("removing element 6:",st.remove(6))

s1 = {2,3,4,5,6}
s2 = {5,6,7,8,9,1}
print(s1,s2)
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.symmetric_difference(s2))
print(s1.symmetric_difference_update(s2))
print(s1.union(s2))
s2.update(s1)
print(s2)





