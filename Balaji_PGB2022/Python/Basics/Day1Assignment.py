#Define variables for each data type
varint    = 50
varfloat  = 18.976
varstring = "coMakeIt"
varchar   = 'A'
boolean=True
print("Integer value is",varint)
intid=id(varint)
print("Float value is",varfloat)
floatid=id(varfloat)
print("String value is",varstring)
strid=id(varstring)
print("Character value is",varchar)
charid=id(varchar)
print("Boolean value is",boolean)
booleanid=id(boolean)

#modify the data
varint    =varint+ 40
varfloat  = varfloat+30.098
varstring=varstring+"Company"
varchar   =varchar+'B'
print("Integer value after modifying is",varint)
intid1=id(varint)
print("Float value after modifying is",varfloat)
floatid1=id(varfloat)
print("String value after modifying is",varstring)
strid1=id(varstring)
print("Chararcter value after modifying is",varchar)
charid1=id(varchar)
print("Boolean value after modifying is",boolean)
booleanid1=id(boolean)
l=[1,2,3]
lid1=id(l)
l[2]=4
lid2=id(l)

#Checking Mutability and immutability
if(intid!=intid1):
    print("Integer is Immutable")
else:
    print("Integer is mutable")
if(floatid!=floatid1):
    print("Float is Immutable")
else:
    print("Float is mutable")
if(strid!=strid1):
    print("String is Immutable")
else:
    print("String is mutable")
if(charid!=charid1):
    print("Character is Immutable")
else:
    print("Character is mutable")

if (lid1 != lid2):
    print("List is Immutable")
else:
    print("List is mutable")

#Assigning Multiple Values and Overriding
x,y=10,20
y="Aurobindo"
print(x)
print(y)

#store int and string type using +
try:
    a=50+"Akhil"
except:
    print("String cannot be added to int")

#store string and boolean type using +
try:
    b="Nithish"+True
except:
    print("String cannot be added to boolean")

#store list and tuple type using +
try:
    c=[10,20,30]+(40,50,60)
except:
     print("list cannot be added to tuple")

company=['Google','Microsoft','coMakeIt','coMakeIt']
place=['California','Mexico','Hyderabad']
print("Actual LIst",company)
company.append("Qualcomm")
print("After appending",company)
#copying company list to company_cp
company_cp=company.copy()
print(company_cp)
#counting number of times element appeared
counter=company.count('coMakeIt')
print(counter)
#Adding both the lists
newlist=company+place
print("Adding both the lists",newlist)
#printing the position of element
print("Position Of element is",company.index("Google"))
#inserting second element at company list
company.insert(1,"DBS")
print("After inserting",company)
#Removing second element
company.pop(1)
print("After removing second element",company)
#Removing one element
company.remove("coMakeIt")
print("After removing",company)
#Reverse the list
company.reverse()
print("After reversing",company)
#Sorting the list
place.sort()
print("After sorting the list",place)

company.clear()
print("After removing all elements",company)


#String Manupulations
#Create String
string="Snookers"
print(string)
#UpperCase
print("Converting string to upper is",string.upper())
#LowerCase
print("Converting string to lower is",string.lower())
#Return count of specified value
print("Count of specified value",string.count('o'))
#Returns true if string ends with true
print("String ends with s",string.endswith('s'))
print("String ends with b",string.endswith('b'))
#Returns true if string has alphabets
print("Is string contains only alphabets?",string.isalpha())
#convert first char to uppercase
print("Converting first char to upper case is ",string.capitalize())
#Searching for specified value
print("Index of Specified value is",string.index('n'))
#Reverse using slicing
print("Reversing the string using slicing",string[::-1])

#Tuple mainpulations
#Create Tupple
tuple=(10,20,30,40,50,40,10,60)
#Return number of times value repeated
print("Count of specified element from tuple",tuple.count(40))
#Searching for specified value
print("Index of Specified value from tuple is",tuple.index(50))

#Creating Dictionary
tup=(1,2,3)
#t=(5,5,5)
l=[5]
print("Creating dictionary",dict.fromkeys(tup,5))
#print("Creating dictionary",dict(zip(tup,l*3)))
tupp=(10,20,30)
l=[5,4,3]
d=dict(zip(tupp,l))
print("Creating onemore dictionary",d)
#Return specified value
print("Value of specified key is",d.get(30))
#print all elements
print("Printing key,value pairs")
for k,v in d.items():
    print("key",k,"Value",v)

#print(d.items())

#Remove specified element
print("Removing specified element from dictionary is",d.pop(20))
print("Printing dictionary after removing specific value",d)
#Remove last inserted value
print("Removing last element value",d.popitem())
print("After removing last item",d)

#Set Manipulations
#Creating Set
set={10,20,30,40,50}
print("Creating set",set)
#Adding element in set
set.add(60)
print("Printing the set after adding the element",set)
#Removing the element from set
set.remove(50)
print("Printing the set after removing the element",set)

set1={1,2,3,4,5}
set2={5,6,7,8,9}
print("set that contains the items that only exist in set1, and not in set2",set1.difference(set2))
print("Removing common elements from two sets")
print("After removing common elements",set1.symmetric_difference(set2))
#set1^set2
#disjoint
print(set1.isdisjoint(set2))
#Return True if all items in set x are present in set y
print("Is set1 is subset of set2?",set1.issubset(set2))
print("Is set2 is subset of set1?",set2.issubset(set1))
#print(set1.issuperset(set2))
print("After removing common elements",set1.symmetric_difference(set2))
print("Remove the items that are present in both sets, AND insert the items that is not present in both sets",set1.symmetric_difference_update(set2))
#set that contains all items from both sets, duplicates are excluded
print(set1.union(set2))
#Inserting elements from one set to another set
set2.update(set1)
print("After Inserting",set2)



