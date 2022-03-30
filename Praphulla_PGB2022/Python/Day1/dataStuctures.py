print("\nNumeric DataTypes in Python:")
var1 = 10
print("\nType of var1: ", type(var1))
var2 = 10.0
print("\nType of var2: ", type(var2))
var3 = 1 + 7j
print("\nType of var3: ", type(var3))
print("\nSequence DataTypes in Python:\n")
msg = "I'm Praphulla"
print("\n Printing Message:", msg)
print("\nType of String", type(msg))
print("\n Checking String immutability:")
try:
    msg[0] = 'p'
    print(msg)
except TypeError:
    print("\n Exception occurred, Strings are immutable!")
Name = "Praphulla"
s = "Age is"
x = 21
b = True
y = str(x)
l = ["Praphulla", "Gumma"]
t = ("CMIT", 1072),  20, "Hyderabad"
res = t + tuple(l)
print("\n Printing Result: ", res)
print(s + " " + y)
print("{} {}".format(s, x))
print(s + " " + str(b))
print("{} {}".format(s, b))
# Creating a List
print("\n Python List Operations:")
List = []
print("\n Initialising a blank List: ", List)
# the use of a String 
List1 = ['Hello! Praphulla']
print("\n Printing a List with the use of a String: ", List1)
# Creating a List with 
# the use of multiple values 
List2 = ["I", "am", "Luna"]
print("\n Printing a List containing multiple values: ", List2)
print("\n Printing First Element:", List2[0])
print("\n Printing First Element:", List2[2])
List3 = [['I', 'am'], ['Luna', 'Lovegood']]
print("\n Printing Multi-Dimensional List: ", List3)
print("\n Printing the first item of the List", List3[0])
print("\n Printing the third item of the List", List3[1])
print("\n Accessing element using negative indexing:", List3[-1], List3[-2])
print("\n Python Tuples Operations:")
Tuple1 = ()
print("\n Initial empty Tuple: ", Tuple1)
Tuple2 = ('Hello!', 'Welcome!')
print("\n Checking Tuple immutability:")
Tuple7= (0, 1, 2, 3)
try:
    Tuple7[0] = 4
    print(Tuple7)
except TypeError:
    print("\n exception caught, Tuples are immutable.")
print("\n Tuple with the use of String: ", Tuple2)
list3 = [1, 2, 4, 5, 6]
print("\n Tuple using List: ")
print(tuple(list3))
Tuple3 = tuple('HarryPotter')
print("\n Tuple with the use of function: ", Tuple3)
Tuple4 = (0, 1, 2, 3)
Tuple5 = ('python', 'Test')
Tuple6 = (Tuple4, Tuple5)
print("\n Tuple with nested tuples: ", Tuple6)
#Boolean dataType
print("\n Boolean DataType in Python:")
print(type(True))
print(type(False))
# create a list fruits = ['apple', 'banana', 'cherry'], cars = ['Ford', 'BMW', 'Volvo']
#PYTHON LISTS EXAMPLE: FRUITS
print("\n List Operations Example:")
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.append('mango')
fruits.append('orange')
print("\n After adding new fruits:")
print("\n List Items: ", fruits)
fruits.insert(2, 'berry')
print("\n After performing Insert Operation on Fruits: ", fruits)
print("\n Initial List: ", fruits)
print("\n List after Removal of two elements: ", fruits.remove('apple'), fruits.remove('mango') )
print("\n List after Removing all the elements: ", fruits.clear())
fruits1 = fruits.copy()
print("\n Copying contents of fruits to fruits1", fruits1)
print("\n Appending elements to the list fruits1", fruits1.append("raspberry"), fruits1.append("cherry"), fruits1.append("blueberry"), fruits1.append("cherry"), fruits1.append("banana"), fruits1)
print("\n The total number of occurrences of the word cherry:", fruits1.count('cherry'))
print("\n Printing the elements of the List Car:",cars)
print("\n Adding two lists Fruits1 and Cars..")
fruits1 = fruits1+cars
print("\n Mixed:", fruits1)
print("\n Position value of cherry", fruits1.index('cherry'))
print("\n Inserting orange as the second element:", fruits1.insert(1, 'orange'), fruits1)
print("\n Removing second element of the list fruits1:", fruits1.pop(1), fruits1)
print("\n Removing Banana from the list", fruits1.remove('banana'), fruits1)
print("\n Reversing the elements in the list fruits1:", fruits1.reverse(), fruits1)
print("\n Sorting the elements in the list fruits1:", fruits1.sort(), fruits1)
#Python Strings
print("\n Python String Operations:")
s = "heLlo world1"
print("\n Input String:", s)
print("\n Converting to upper case", s.upper())
print("\n Converting to lower case", s.lower())
print("\n The number of times 'l' occurs in the string:", s.count('l'))
print("\n The string ends with 'd' ", s.endswith('d'))
print("\n Whether the string contains all alphabets", s.isalpha())
print("\n Capitalising th first letter:", s, s.capitalize())
print("\n Converting the first character of each word to upper case", s,  s.title())
print("\n Searching the string for a specified value and returns the position of where it was found", s, s.rfind('w'))
print("\n Revering the string with slicing", s[::-1], s)
#Python Tuples
print("\n Python Tuples Operations:")
t = ('Hi', 'Hello', 'Welcome', 'Bye', 'Hi')
print("\n Return the number of times 'Hi' occurs in a tuple", t.count('Hi'))
print("\n Searching the tuple for 'Hello' and returns the position of where it was found", t.index('Hello'))
#Python Dictionaries
print("\n Python Dictionary Operations")
d = {"Espresso": "coffee", "Capuccino": "coffee", "Americano": "coffee"}
print(d)
t1 = 'Praph','Raphy', 'Luna'
t2 = 5
d1 = {}
print("\n A dictionary with 3 different keys, all with the value '5':", d1.fromkeys(t1, t2))
print("\n Return the value of the specified key in a Dictionary:", d.get('coffee'))
print("\n Print all key, value pairs ", d.items())
print("\n Removing elements from a particular position:", d.pop('Americano'), d)
print("\n Removing the last inserted key-value pair:", d.popitem(), d)
#Python Sets
print("\n Python Set Operations:")
s = {"animals", "birds", "reptiles"}
print("\n Printing set of elements:", s)
print("\n Adding an element to a set:", s.add("humans"), s)
print("\n Removing a specific element:", s.remove('animals'), s)
#2sets
x = {(1, 2, 3, 4, 5, 6, 7, 8)}
y = {(2, 4, 6, 8, 10)}
print(type(x))
print("\n Return a set that contains the items that only exist in set x, and not in set y", x.difference(x,y))
print("\n Adding an element to the set:", x.add(11), x)
print("\n updating set x", x.update(y), x)
print("\n Discarding an element from the set:", x.discard("10"))
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6}
print("\n Set Difference:", a.difference(b))
print("\n Set Difference:", b.difference(a))
print("\n Set Intersection:", a.intersection(b))
print("\n Checking if two sets are disjoint:", a.isdisjoint(b))
z = a.symmetric_difference(b)
print("\n Whether there is a symmetric difference:", z)
print("\n Super set:", a.issuperset(b))
print("\n Sub set:", b.issubset(a))
print("\n Set Union", a.union(b))
print("\n Set Update:", a.update(b), a)
print("\n symmetric_difference_update" ,a.symmetric_difference_update(b),a )
