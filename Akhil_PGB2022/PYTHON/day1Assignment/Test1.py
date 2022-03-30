#Defining variables for each data type 
x = "Smash"
y = 45.546
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
s = "kim"
print("Address of s:",id(s))
s = s+"Jong"
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
	a = 5+"NIthish" 
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
#List
print("List")
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
print("Actual fruit list ",fruits)
print("Cars list ",cars)
fruits.append('mango')
print("After Appending ",fruits)
fruits_cp = fruits.copy()
print("Fruits copy: ",fruits_cp)
fruits_cp.clear()
print("After removing all fruits", fruits_cp)
print("Frequency of Cherry: ",fruits.count('cherry'))
fruits = fruits+cars
print("Concatenating Lists: ",fruits)
print("Position of cherry:",fruits.index('cherry'))
fruits.insert(1,'orange')
print("After inserting Orange:",fruits)
fruits.pop(1)
print("After Removing the second element: ",fruits)
fruits.remove('banana')
print("After removing banana: ",fruits)
fruits.reverse()
print("After reversing list: ",fruits)
cars.sort()
print("After sorintg cars: ",cars)
print()

#String
s = "coMakeIT company"
print("String:",s)
print("String UpperCase: ",s.upper())
print("String LowerCase: ",s.lower())
print("Frequency of 'a': ",s.count('a'))
print("Check String ends with 'any' :",s.endswith('any'))
print("Check string is in uppercase: ",s.isupper())
print("convert the first character of each word to upper case:",s.title())
print("Convert the first character to upper case :",s.capitalize())
print("Check all characters in the string are in the alphabet:",s.isalpha())
print("Character position: ",s.index('n'))
print("Reversing string with slicing: ",s[::-1])
print()

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

#set
st = {3,5,6,8,2,0,1}
print("Set: ",st)
print("Adding elements to set: ",st.add(23))
print("removing element 6:",st.remove(6))

s1 = {2,3,4,5,6}
s2 = {5,6,7,8,9,1}
print("Sets:",s1,s2)
print("Return a set that contains the items that only exist in set s1, and not in set s2:",s1.difference(s2))
print("Remove the items that exist in both sets:",s1.symmetric_difference(s2))
print("Return True if no items in set s1 is present in set s2: ",s1.isdisjoint(s2))
print("Return True if all items in set s1 are present in set s2:", s1.issubset(s2))
print("Return True if all items in set s2 are present in set s1:", s1.issuperset(s2))
print("Return a set that contains all items from both sets, except items that are present in both sets: ",s1.symmetric_difference(s2))
print("Remove the items that are present in both sets, AND insert the items that is not present in both sets: ",s1.symmetric_difference_update(s2))
print("Return a set that contains all items from both sets, duplicates are excluded: ",s1.union(s2))
s2.update(s1)
print("Insert the items from set s2 into set s1:",s2)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
