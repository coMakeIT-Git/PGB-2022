#Defining variables for each data type
x="cmit"
y=4.56
p=True
q=56
b='A'

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

s = "nithish"
print("Address of s:",id(s))
s = s+"kumar"
print("Address of s:",id(s))
print("As the addresses are different Strings and other datatypes are immutable")
print()

#Assign multiple values and override the data types

print("Assign multiple values and override the data types")
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
	a = 5+"iIthish"
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

#---------------------------------------------------------------------------------------------------
#list operations

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.append('carrot')
print("after adding element to fruits: ",fruits)

fruits_copy=fruits.copy()
fruits.clear()
print("after removing all elements from fruits: ",fruits)
print("after copying all elements from fruits: ",fruits_copy)
print("no.of times cherry appears in fruits: ",fruits_copy.count('cherry'))

fruits_copy=fruits_copy+cars
print("adding cars to fruits: ",fruits_copy)
print("position of cherry: ",fruits_copy.index('cherry'))

fruits_copy.insert(1,'orange')
print("after inserting orange as 2nd element: ",fruits_copy)

fruits_copy.pop(1)
print("after removing 2nd element: ",fruits_copy)

fruits_copy.remove('banana')
print("after removing banana: ",fruits_copy)

fruits_copy.reverse()
print("after reversing fruits list: ",fruits_copy)

cars.sort()
print("after sorting cars list: ",cars)
print()
#----------------------------------------------------------------------------------------------------
#String operations

name='continuous innovation'
print("string: ",name)
print("converting to upper case: ",name.upper())
print("converting to lower case: ",name.lower())
print("number of times n occurs in string: ",name.count('n'))
print("checking string ends with ion: ",name.endswith('ion'))
print("checking all characters are in alphabet: ",name.isalpha())
print("converting each char of first word to upper case: ",name.title())
print("converting first char to upper case: ",name.capitalize())
print("searching for value and print position: ",name.find('ion'))
print("reverse string eith sliciing: ",name[::-1])
print()

#---------------------------------------------------------------------------------------------------
#tuple operations

tuple=(3,5,7,11,7,13,17,19)
print("no.of times value 7 occur in tuple: ",tuple.count(7))
print("search 13 and return position: ",tuple.index(11))
print()

#---------------------------------------------------------------------------------------------------
#dictionary operation

k=['one','two','three']
v=[5]
d=dict.fromkeys(k,v)
print("printing dictionary: ",d)

print("printing value of one: ",d.get('one'))
print("printing all key value pairs: ")
for i,j in d.items():
    print("key: ",i," value: ",j)

d.pop('two')
print("after removing two: ",d)

d.popitem()
print("after removing last index: ",d)
print()

#---------------------------------------------------------------------------------------------------
#set operation

set={6,2,5,0,3,1,7,4}
print("printing set: ",set)

set.add(9)
print("printing set after adding 9: ",set)

set.remove(9)
print("printing set after removing 9: ",set)

x={3,6,0,9,2}
y={6,8,0,2,4}
print("sets :",x,y)
print("printing set that contains the items that only exist in set x, and not in set y: ",x.difference(y))
common=x.intersection(y)
print("printing items that exist in both sets: ",common)

print("checking if no items in set x is present in set y: ",x.isdisjoint(y))
print("checking if all items in set x are present in set y: ",x.issuperset(y))
print("checking if all items in set y are present in set x: ",y.issuperset(x))
print("printing a set that contains all items from both sets, except items that are present in both sets: ",x.symmetric_difference(y))
print("Remove the items that are present in both sets, AND insert the items that is not present in both sets: ",x.symmetric_difference_update(y))
print("Returning a set that contains all items from both sets, duplicates are excluded: ",x.union(y))
y.update(x)
print("after insert the items from set y into set x: ",y)