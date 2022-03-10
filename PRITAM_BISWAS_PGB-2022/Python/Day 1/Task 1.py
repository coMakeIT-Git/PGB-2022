"""
Types of datatypes
    1.Numbers - integer, complex , float
    2.Sequence Type - string, list , tuple
    3.Boolean
    4.Set
    5.Dictionary
"""
a=20
sp="Pritam"
c=10.5
d=1+3j
list1= ['cat', 'dog', 'bunny']
tup=("hi", "Python", 2)
d ={1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}
set2 = set()
set2 = {'James', 2, 3,'Python'}
print(type(a))
print(type(sp))
print(type(c))
print(type(d))
print(type(list1))
print(type(tup))
print(type(d))
print(type(True))
print(type(set2))

"""
Mutable objects: list, dict, set  (changed)
Imutable objects: int, float, bool, string, unicode, tuple (can not be changed)

These are of in-built types like int, float, bool, string, unicode, tuple.
In simple words, an immutable object can’t be changed after it is created.
  
The mutable objects can be changed to any value or state without adding a new object.
Whereas, the immutable objects can not be changed to its value or state once it is created. 
"""
"""
Tuple vs list
Tuple: immutable , iteration faster , consume less memory , less built-in function 
List : mutable , iteration slower , consume more memory , many built in function

why tuple is faster than list?
Ans:Tuples are stored in a single block of memory. 
Tuples are immutable so, It doesn't require extra space to store new objects. 
Lists are allocated in two blocks: the fixed one with all the Python object information
and a variable sized block for the data. It is the reason creating a tuple is faster than List.
"""
# Modify specific element in list nd dict
list1[0]='sugar glider'
print(list1)
d[1] = "John"
print(d)
"""
Set elements are unique. Duplicate elements are not allowed. 
A set itself may be modified, but the elements contained in the set must be of an immutable type.
"""


#Immutable objects - int, float, bool, string, unicode, tuple
phrase = 'Hello world'
#phrase[0]="hi"
print(phrase)

#Create variables and assign multiple values and override the data types

a=10
print(a)
a=10.5
print(a)

"""Define variable 'a' and store int and string types using + operator 
to resolve we need  to use 
1.str() function : print(s + str(y))
2.Using % Operator: print("%s%s" % (s, y))
3.Using format() function: print("{}{}".format(s, y))
4.Using f-strings:  print(f'{s}{y}')
"""
s = "Year is "
y = 2018
print(s + str(y))

""" Define variable 'b' and store string and boolean types using + operator
to resolve we need  to use 
1.str() function : print(s + str(y))
2.Using % Operator: print("%s%s" % (s, y))
3.Using format() function: print("{}{}".format(s, y))
4.Using f-strings:  print(f'{s}{y}')
"""
k= "Yes it is  "
m = True
print(k + str(m))

"""
Define variable 'c' and store list and tuple types using + operator 
to resolve we need to use 
1. use list : print(list1+list(tup))
2. use tuple : print(tuple(list1)+tup)
"""

list1= ['cat', 'dog', 'bunny']
tup=("hi", "Python", 2)

print(list1+list(tup))

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
# To add elements in list use append() function
fruits.append("orange")
# To clear elements in list use clear() function
fruits.clear()
#Copy the fruits list using copy() function
fruits = ['apple', 'banana', 'cherry']
numb = fruits.copy()
print(numb)

# Return the number of times the value "cherry" appears in the fruits list using count() function
counter_b=fruits.count('cherry')
print(counter_b)
# Add the elements of cars to the fruits list using extend
fruits.extend(cars)
print(fruits)
# find the position of the value "cherry" using index() function
print(fruits.index("cherry"))
#Insert the value "orange" as the second element of the fruit list using insert() function
fruits.insert(1,"orange")
print(fruits)
#Remove the second element of the fruit list using pop() or del method
#fruits.pop(1)
del fruits[1]
print(fruits)
#Remove the "banana" element of the fruit list using remove
fruits.remove("banana")
print(fruits)
# Reverse the order of the fruit list
fruits.reverse()
print(fruits)
# Sort the cars list using sort() function
cars.sort()
print(cars)

#Create a string
name="Pritam Biswas"
"""
1.The functions isupper() and islower() returns the boolean True value 
if the all the characters of the string are in upper case or lower case respectively.
2.The functions upper() and lower() returns the string by converting all the characters 
of the string to upper case or lower case respectively
"""
# Convert it into upper case using upper()
print(name.upper())
# Convert it into lower case using lower()
print(name.lower())

#Return the number of times a specified value occurs in a string
import re
str1 = 'John has 1 apple, Sarah has 2 apples, Mike has 5 apples.'
substr = 'apples'
# Use re.finditer() to find all substring occurrences
# Using list comprehension we find the start and end indices of every substring occurence
result = [(_.start(), _.end()) for _ in re.finditer(substr, str1)]
print("Number of substring occurrences is:", len(result))

"""Return true if the string ends with the specified value

string.endswith(value, start, end)
value : Required. The value to check if the string ends with
start : Optional. An Integer specifying at which position to start the search
end   : Optional. An Integer specifying at which position to end the search
"""
txt = "hello, welcome to my world."
x = txt.endswith(".")
print(x)
"""
Return True if all characters in the string are in the alphabet
The isalpha() method returns True if all characters in the string are alphabets.
If not, it returns False.
"""
string="helloworld"
print(string.isalpha())
# Convert the first character of each word to upper case using title() function
print(txt.title())
# Convert the first character to upper case using capatilized() function
print(txt.capitalize())
#Search the string for a specified value and returns the position of where it was found using index() function
print(str1.index("apple"))
""" Reverse the string with slicing
1.slicing: Strings can be reversed using slicing. To reverse a string, 
we simply create a slice that starts with the length of the string, and ends at index 0.

2.slice() function : returns a slice object.
slice(start, end, step)
start :	Optional. An integer number specifying at which position to start the slicing. Default is 0
end   :	An integer number specifying at which position to end the slicing
step  : Optional. An integer number specifying the step of the slicing. Default is 1
"""
print(str1[::-1])
#Create a tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
#Return the number of times a specified value occurs in a tuple using count() function
x = thistuple.count(5)
print(x)
#search the tuple for a specified value and returns the position of where it was found
ab= thistuple.index(5)
print(ab)
"""
Dictionary is an unordered collection of data values, used to store data values 
like a map, which, unlike other Data Types that hold only a single value as an element, 
Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.

syntax: dictionaryname={key: value}
example: {1: [1, 2, 3, 4], 'Name': 'Geeks'}
"""

#Create a dictionary with 3 different keys, all with the value '5' using inbuilt method
keys = {'a', 'e', 'i', 'o', 'u' }
value=5
vowels = dict.fromkeys(keys,value)
print(vowels)
"""Create a dictionary  and and apply respective inbuilt method to 
1.Return the value of the specified key : dictionary.get(keyname, value) or dictionary(keyname)
2. Print all key, value pairs
3. Remove the element with the specified key : pop()
4. Remove the last inserted key-value pair : popitem()
"""
print(dict1.get("geeks"))
print(dict1)
dict1.pop("geeks")
print(dict1)
D = {'name': 'Bob', 'age': 25}
v = D.popitem()
print(D)


"""
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
1. Duplicates Not Allowed: Sets cannot have two items with the same value.
2. Unordered means that the items in a set do not have a defined order.
3. Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Syntax: setname={ value1, value2, value3 }
Example:  set1 = {"apple", "banana", "cherry"}

Python Collections (Arrays)
There are four collection data types in the Python programming language:
    1.List is a collection which is ordered and changeable. Allows duplicate members.
    2.Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    3.Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    4.Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
# Create a Set
set1 = {"apple", "banana", "cherry"}
#Add an element to the set using add() function
set1.add("orange")
print(set1)
#Remove specific element using remove()
set1.remove("cherry")
print(set1)

#create 2 sets x and y
x={"apple", "banana", "cherry"}
y={'apple', 'cherry', 'Ford', 'BMW', 'Volvo'}

"""" 
Return a set that contains the items that only exist in set x, and not in set y
---------------------------------------------------------------------------------
The difference() method returns a set that contains the difference between two sets.

Syntax:  set.difference(set)
set: Required. The set to check for differences in

"""
z = x.difference(y)
print(z)
""" Remove the items that exist in both sets
----------------------------------------------------------------------------------
The intersection() method returns a set that contains the similarity between two or more sets.

Syntax : 
set.intersection(set1, set2 ... etc)
set1 :	Required. The set to search for equal items in
set2 :	Optional. The other set to search for equal items in.

"""
z=set.intersection(x,y)
print(x-z)
print(y-z)
"""
Return True if no items in set x is present in set y
----------------------------------------------------------------------
The isdisjoint() method returns True if none of the items are present in both sets,
otherwise it returns False.
Syntax :  set.isdisjoint(set)
set : Required. The set to search for equal items in

"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

""" 
Return True if all items in set x are present in set y
----------------------------------------------------------------------------------
The issubset() method returns True if all items in the set exists in the specified set,
otherwise it retuns False.

Syntax: set.issubset(set)
set :	Required. The set to search for equal items in
"""
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
""" Return True if all items set y are present in set x
----------------------------------------------------------------------------------
The issuperset() method returns True if all items in the specified set exists in the
original set, otherwise it retuns False.

Syntax: set.issuperset(set)
set : Required. The set to search for equal items in
"""
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
"""Return a set that contains all items from both sets, except items that are present in both sets
-------------------------------------------------------------------------------------------------
The symmetric_difference() method returns a set that contains all items from both set, but not the 
items that are present in both sets.

Syntax:  set.symmetric_difference(set)
set : Required. The set to check for matches in
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
"""Remove the items that are present in both sets, AND insert the items that is not present in both sets
--------------------------------------------------------------------------------------------------------
The symmetric_difference_update() method updates the original set by removing items that are present in 
both sets, and inserting the other items.

Syntax: set.symmetric_difference_update(set)
set : Required. The set to check for matches in
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
"""Return a set that contains all items from both sets, duplicates are excluded
------------------------------------------------------------------------------------------------------
The union() method returns a set that contains all items from the original set, and all items from the
specified set(s).

Syntax: set.union(set1, set2...)
set1 : Required. The iterable to unify with
set2 : Optional. The other iterable to unify with.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
""" Insert the items from set y into set x
------------------------------------------------------------------------------------------------------
The update() method updates the current set, by adding items from another set (or any other iterable).

Syntax : set.update(set)
set : Required. The iterable insert into the current set

"""
x.update(y)
print(x)
