Different datatypes in python

5 <class 'int'>
adithya <class 'str'>
5.2 <class 'float'>
True <class 'bool'>

overriding the variables

a is overriding from integer to string  abc
a is overriding from string to list  [1, 2, 3]
a is overriding from list to tuple  (1, 2, 3)
a is overriding from tuple to Dictionary  {1: 'a', 2: 'b'}

mutable and immutable datatypes 

address of list before  139947480170880
address of list after 139947480170880
As address of list doesn't change on list Operations, list is mutable 

address of tuple before  139947479688064
address of tuple after  139947479299712
As address of tuple changed on tuple Operations, tuple is immutable 

address of Dictionary before  139947479688576
address of Dictionary after  139947479688576
As address of Dictionary doesn't change on Dictionary Operations, Dictionary is mutable 

address of set before 139947479271232
address of set after  139947479271232
As address of set doesn't change on set Operations, set is mutable 


Adding different datatypes

String and Integer cannot be added
string and boolean cannot be added
List and Tuple cannot be added

List Operations

fruit list after adding new element:  ['apple', 'banana', 'cherry', 'pineapple']
New copy of fruits list:  ['apple', 'banana', 'cherry', 'pineapple']
cherry count in fruits list:  1
car elements added to fruits list:  ['apple', 'banana', 'cherry', 'pineapple', 'Ford', 'BMW', 'Volvo']
index of cherry in fruits:  2
Fruits list after inserting oranges at first index:  ['apple', 'orange', 'banana', 'cherry', 'pineapple', 'Ford', 'BMW', 'Volvo']
Fruits list after removing element at position 1  ['apple', 'banana', 'cherry', 'pineapple', 'Ford', 'BMW', 'Volvo']
Fruits list after removing banana  ['apple', 'cherry', 'pineapple', 'Ford', 'BMW', 'Volvo']
Fruits list after reversing  ['Volvo', 'BMW', 'Ford', 'pineapple', 'cherry', 'apple']
Cars list after sorting  ['BMW', 'Ford', 'Volvo']

String Operations

String after converting it into uppercase  RAVI TEJA
String after converting it into lowercase  ravi teja
Count of character a in String is  2
String ends with a:  True
All characters in String are alphabets  False
Words in String Starts with uppercase ['Ravi', 'Teja']
String first character changed to uppercase  Ravi teja
Index of a in String 1
reversing the string using slicing ajet ivaR

Tuple Operations

Tuple:  ('amar', 'akbar', 'antony')
Count of amar in tuple:  1
Index of Akbar in tuple:  1

Dictionary Operations

Dictionary created using tuples {'apple': 5, 'banana': 5, 'mango': 5}
Retriving value of key apple:  5
Key And Value in Dictionary  apple 5
Key And Value in Dictionary  banana 5
Key And Value in Dictionary  mango 5
Dictionary after poping apple key  {'banana': 5, 'mango': 5}
Dictionary after poping last key  {'banana': 5}

Set Operations

Set after adding a element {1, 2, 3, 4}
Set after removing element {2, 3, 4}
Set that consists only elements of x but not in y  {2, 3}
Sets after removing common elements of both  {2, 3} {4, 5}
Return True if no items in set x is present in set y:  True
Return True if all items in set x are present in set y: False
Return True if all items in set y are present in set x: False
Return a set that contains all items from both sets, except items that are present in both sets:  {2, 3, 4, 5}
Remove the items that are present in both sets, AND insert the items that is not present in both sets:  None
Return a set that contains all items from both sets, duplicates are excluded:  {2, 3, 4, 5}
Insert the items from set y into set x: {2, 3, 4, 5}
