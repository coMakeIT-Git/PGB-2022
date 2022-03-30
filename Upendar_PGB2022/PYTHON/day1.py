# 2 Defining variables for each datatype
id = 181
name = "upendar"
salary = 20000.50
print(id)
print(name)
print(salary)
print(type(id))
print(type(name))
print(type(salary))

# 3 modify the data and identify which data types are mutable and which are immutable
list2 = ["rakesh" , "naveen" , "sai"]
list2[0]="sita"
print(list2)
tupple1 =("rakesh" , "naveen" , "sai")

# 4 Creating variable and assign multiple values and override the data types
var=10
var="ram"
var=100.10
print(var)

# 5a Define variable 'a' and store int and string types using + operator
a = str(101) + "ram"     #resolved by typecasting
print(a)

# 5b Define variable 'b' and store string and boolean types using + operator
b = "ram" + str(True)    #resolved by typecasting
print(b)

# 5c define variable 'c' and store list and tuple types using + operator
c = list2 + list(tupple1)
print(c)

# 6 create list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.append('mango')              #adding element
fruits1=fruits.copy()               #copying list
fruits.clear()                      #clearing list items
print(fruits1)
fruits1.extend(cars)            #adding 2 lists
print(fruits1)
print(fruits1.count("cherry"))       #return no of times values
print(fruits1.index("cherry"))      #position of element
fruits1.insert(1, "orange")
print(fruits1)
#remove element at index2
fruits1.pop(1)
print(fruits1)
# remove element
fruits1.remove("banana")
print(fruits1)
# reverse list
fruits1.reverse()
print(fruits1)
# sort cars list
cars.sort()
print(cars)
###################################################
# 7 create string
a = "Hello world"
print(a)
print(a.upper())             # a Convert it into upper case
print(a.lower())             # b Convert it into lower case
print(a.title())             # f convert the first character of each word to upper case
print(a.capitalize())        # g Convert the first character to upper case
print(a.count('o'))          # c Return the number of times a specified value occurs in a string
print(a.endswith('d'))       # d Return true if the string ends with the specified value
print(a.isalpha())           # e Return True if all characters in the string are in the alphabet
print(a.find('e'))           # h Search the string for a specified value and returns the position of where it was found
print(a[::-1])               # i Reverse the string with slicing

#########################################################
# 8 create tuple

thistuple = ("upendar", "sai", "varun")
print(thistuple)
print(thistuple.count('sai'))       #Return the number of times a specified value occurs in a tuple
print(thistuple.index('varun'))     #search the tuple for a specified value and returns the position of where it was found

#########################################################
# 9 dictionary
thisdict = "key1","key2","key3"     #Create a dictionary with 3 different keys, all with the value '5' using inbuilt method
dict1=dict.fromkeys(thisdict,5)
print(dict1)
##############################################################
# 10 Dictionary
thisdict1 =	{"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict1["brand"])       # a Return the value of the specified key
thisdict1.items()               # b Print all key, value pairs
print(thisdict1)
thisdict1.pop("model")          # c Remove the element with the specified key
print(thisdict1)
thisdict1.popitem()            # d Remove the last inserted key-value pair
print(thisdict1)

##########################################################33
 # 11 set
thisset = {"student", "employee", "manager"}
print(thisset)
thisset.add("boss")                  # 1  Add an element to the set
print(thisset)
thisset.remove("boss")               # 2 Remove specific element
print(thisset)

#############################################
# 12 2-sets
seta = {1,2,3,4,5,6,7}
setb = {1, 2, 8,9}

print(seta.difference(setb))  # a Return a set that contains the items that only exist in set x, and not in set y
seta.intersection(setb)
seta.difference_update(setb)    # b Remove the items that exist in both set
print(seta)
print(seta.isdisjoint(setb))      # c Return True if no items in set x is present in set y
print(seta.issubset(setb))          # d Return True if all items in set x are present in set y
print(setb.issubset(seta))         # e Return True if all items set y are present in set x
print(seta.symmetric_difference(setb))      # f Return a set that contains all items from both sets, except items that are present in both sets
seta.symmetric_difference_update(setb)      # g Remove the items that are present in both sets, AND insert the items that is not present in both sets
print(seta)
print(seta.union(setb))                 # h Return a set that contains all items from both sets, duplicates are excluded
seta.update(setb)                       # i Insert the items from set y into set x
print(seta)