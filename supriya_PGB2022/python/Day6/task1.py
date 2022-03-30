print("hello python")
#variables of different data types
num=100
print(num)
print(type(num))
s='python'
print(s)
print(type(s))
print(100>20)
print(20>40)
print(100==100)
list=["pyhon","version",3.3,3]
print(list)
print(type(list))
tup=("pyhon","version",3.3,3)
print(tup)
print(type(tup))
dict={'name':'python','version':3.3}
print(dict)
print(type(dict))
set={"python","c","java"}
print(set)
print(type(set))
# finding mutable and immutable datatypes
list1=["pyhon","version",3.3,3]
list1.append("java")
print(list1)
print("List is mutable")
tuple1=("pyhon","version",3.3,3)
#tuple1[2]=1000
#print(tuple1)
print("Tuple is immutable")
dict1={'name':'python','version':3,'version':3.3}
print(dict1)
print("Dictionary is mutable")
set1={"python","c","java"}
set1.add("html")
print(set1)
print("Set is mutable")
#Override datatypes
x, y, z = "Hyderabad", "Chennai", "Delhi"
print(x)
print(y)
print(z)

x = y = z = "Hyderabad"
print(x)
print(y)
print(z)

Places = ["Kashmir", "Tamil Nadu", "Delhi"]
x, y, z = Places
print(x)
print(y)
print(z)
#5. Define variable 'a'and store int and string types using + operator and resolve errors if any
#	define variable 'b' and store string and boolean types using + operator and resolve errors if 
#	define variable 'c' and store list and tuple types using + operator and resolve errors if any
Text = "Tom"
t1 = "Styding in"
a = 10
b = True
y = str(a)
l = ["car", "bike", "chopper"]
t = ("car", 667),  10, "Hyderabad"
c = t + tuple(l)
print(c)
print(t1 + " " + y)
print("{} {}".format(t1, a))
print(t1 + " " + str(b))
print("{} {}".format(t1, b))
#Creating list and applying built-in methods
place=["hyderabad","tamil nadu","maharastra"]
language=["telugu","tamil","hindi"]
place.append("kerala") #adding element to list
print(place)
place.copy() #copies all elements from list
print(place)
#place.clear() #removes all elements from list
#print(place)
print(place.count("hyderabad")) #Return the number of times the value "hyderabad" appears in the fruits list
print(place+language) #Add the elements of language to the place list
print(place.index("kerala") ) #position of the value 
place.insert(2,"karnataka")#Insert the value "karnataka" as the second element of the place list
print(place)
place.pop(2)  # Remove the second element of the  place list
print(place)
place.remove("tamil nadu")#Remove the "tamilnadu" element of the place 
print(place)
place.reverse()#Reverse the order of the place list
print(place)
language.sort()#Sort the language list
print(language)
#Create String
txt="Creating a string in python"
print(txt)
print(txt.upper())#Convert it into upper case
print(txt.lower())        #	 Convert into lower case
print(txt.count("a"))       #Return the number of times a specified value occurs in a string
print(txt.endswith("n"))#Return true if the string ends with the specified value
print(txt.isalpha())#Return True if all characters in the string are in the alphabet #return false as it contains whitespaces
print(txt.title())#Convert the first character of each word to upper case
print(txt.capitalize())#Convert the first character to upper case
print(txt.find("a"))#Search the string for a specified value and returns the position of where it was found
#Create a tuple and
tuple2=("developer",678,"tester",56.7,)
print(tuple2)
print(tuple2.count("tester"))#Return the number of times a specified value occurs in a tuple
print(tuple2.index("tester"))#Search the tuple for a specified value and returns the position of where it was found
#Create a dictionary with 3 different keys, all with the value '5' using inbuilt method
li =['ball', 'bat', 'helmet']
v=5
thisdict = dict.fromkeys(li, v)
print(thisdict)

#Create a dictionary  and and apply respective inbuilt method to
d={'name':'python','version':3,'updatedvr':3.3}
print(d.get('name')) #Return the value of the specified 
print(d)#Print all key, value pairs
print(d.pop('version'))#Remove the element with the specified key
print(d.popitem())# Remove the last inserted key-value pair
#Create a Set and apply inbuild methods to
set2={"c","java","python","html"}
print(set2)
set2.add("css")#Add an element to the set
print(set2)
set2.discard("html")#Remove specific element
print(set2)
# create 2 sets x and y 
x1={'c','java','python'}
y1={'html','python','css'}
print(x1)
print(y1)
print(x1.difference(y1))#Return a set that contains the items that only exist in set x, and not in set y
print(x1^y1)#Remove the items that exist in both 
print(x1.isdisjoint(y1))#Return True if no items in set x is present in set y
print(y1.issuperset(x1))#Return True if all items in set x are present in set 
print(x1.issuperset(y1))#Return True if all items set y are present in set x
print(x1^y1)#Return a set that contains all items from both sets, except items that are present in both sets
res=x1^y1   #Remove the items that are present in both sets, AND insert the items that is not present in both sets
z = x1.intersection(y1)
res.update(z)
print(res)

print(x1.union(y1))#Return a set that contains all items from both sets, duplicates are excluded
x1.update(y1)#Insert the items from set y into set x
print(x1)