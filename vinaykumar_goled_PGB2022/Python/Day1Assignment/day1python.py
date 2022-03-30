#Task 1
#Numeric type
i = 5
print("Type of a:", type(i))
i = 10
print(i)
f = 5.0
print("Type of b:", type(f))
f = 10.0
print(f)
com = 2+4j
print("Type of c:", type(com))
com = 1+19j
print(com)
#Sequence type
string = "Hello everyone"
print("Type of string:", type(string))
print(string)
string = "Hello"
print(string)
#List
List = ["Vinay","Ram","Harish","Girish"]
print(type(List))
print("List before modification:", List)
List.append("Krishna")
print("List after modification:", List)
#Tuple
Tuple = ("Vinay","Ram","Harish","Girish")
print(type(Tuple))
print("Tuples are immutable!")
print(Tuple)
#boolean
bol1 = True
print(type(bol1))
bol2 = False
print(type(bol2))
#set
set1 = {"Vinay","Ram","Harish","Girish"}
print(type(set1))
print("Set before modification:", set1)
set1.add("Krishna")
set1.add("Vinay")
print("Set cannot have duplicate values")
print("Set after modification: ", set1)
#Dictionary
Dict = {1:"Vinay", 2:"Ram", 3:"Harish", 4:"Girish"}
print(type(Dict))
print("Dictionary before modification:", Dict)
Dict[5] = "Krishna"
print("Dictionary after modification:", Dict)

#Task 4
var1 = 5.0
print(var1)
var1 = True
print(var1)
var1 = "Kishan"
print(var1)

#Task 5
a = str(10) + "Vinay"
print(a)
b = "vinay" + str(True)
print(b)
c = [10, 100, 1000] + list((1, 11, 111))
print(c)

#Task 6
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.append("Mango")
print(fruits)
fruits.remove("apple")
print(fruits)
copied_list = fruits.copy()
print(copied_list)
print("Number of times cherry is present: ",fruits.count("cherry"))
fruits.extend(cars)
print(fruits)
print("Position of cherry: ",fruits.index("cherry"))
fruits.insert(1, "orange")
print(fruits)
fruits.pop(1)
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.reverse()
print(fruits)
cars.sort()
print(cars)

#Task 7
str = "software developer"
print(str.upper())
print(str.lower())
print("Number of times m occurs: ",str.count('m'))
print("String ends with r: ",str.endswith('r'))
print("String has only alphabets in it: ", str.isalpha())
print("Capitalising first character of every word in string: ",str.title())
print("Capitalising first character of first word:",str.capitalize())
print("Last position of r: ",str.rindex('r'))
print("Reverse of a string using splicing: ",str[::-1])

#Task 8
tup = 10,20,30,40,10
print(tup)
print("Number of times 10 occurs in the tuple:",tup.count(10))
print("Position of 20 in the tuple:",tup.index(20))

#Task 9
t1 = 'p','q','r','s'
t2 = 5,5,5
print("Creating a dictionary with 3 keys and value as 5: ",dict(zip(t1,t2)))

#Task 10
mydict = {1:"Ram", 2:"Kishan", 3:"Girish", 4:"Harish"}
print(mydict)
print("Value of second key is: ",mydict.get(2))
print("Printing the key value pairs of dictionary:")
for key, value in mydict.items():
    print(key,':',value)
mydict.pop(2)
print("Removing the element with key as 2: ",mydict)
mydict.popitem()
print("Removing the last inserted key value pair: ",mydict)

#Task 11
myset = {"Java","Python","Javascript","ReactJS"}
print(myset)
myset.add("AngularJS")
print("Set after adding an element:", myset)
myset.remove("ReactJS")
print("Set after removing an element: ", myset)

#Task 12
x = {"Ram", "Harish", "girish", "Richard"}
y = {"Mohan", "John", "Jacob", "Richard"}
print(x)
print(y)
print("Set containing elements of x only:",x.difference(y))
print("Removing the elements that exist in both the sets:",x.symmetric_difference(y))
print("No items of set x is present in set y:",x.isdisjoint(y))
print("No items of set y is present in set x:",y.isdisjoint(x))
print("all items in set x are present in set y:",x.issubset(y))
print("all items in set y are present in set x",y.issuperset(x))
print("Returning a set that contains all items from both sets, except items that are present in both sets",x.symmetric_difference(y))
x.symmetric_difference_update(y)
print("Removing the items that are present in both sets:",x)
x.add("Pavan")
y.add("Karthik")
x = x.union(y)
print("Set containing all items from both sets except duplicates:", x)
x.update(y)
print("Inserting the elements of set y into set x:",x)








