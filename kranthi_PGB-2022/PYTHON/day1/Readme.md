All datatypes in python out put:

a is of type:   <class 'int'>
b is of type:   <class 'float'>
c is of type:   <class 'complex'>


This is a string  <class 'str'>
 this 
is multiline
string <class 'str'>
['Hi', 'I am', 'List'] <class 'list'>


(0, 1, 2, 3) <class 'tuple'>
('python', 'geek') <class 'tuple'>


True <class 'bool'>
False <class 'bool'>


{'a', 'i', 'T', 't', 'e', 'h', 's', ' '} <class 'set'>
{1: 'dictionay', 2: 'is collection of ', 3: 'key value'} <class 'type'>
{(1, 'hello'), (2, 'kranthi')}
is collection of 

------------------------------------------------------------------------------------------------------------------------------------------------
Using + operator output:

type casting string to int adding int and string
221
type casting bool to string concating string and bool
this isTrue
type casting tuple to list and concating list and tuple
[1, 2, 3, 22, 40]
-----------------------------------------------------------------------------------------------------------------------------------------------------
Mutable immutable datatypes out put:

[1, 3, 5]
id of the first list 140611948306368
<class 'list'>
[8, 3, 5]
id of the updated list 140611948306368
<class 'list'>
both list are having same id hence Lists are mutable
similarly sets and dictionaries are also mutable


21
id of first created age 9789632
<class 'int'>
22
id of second created age 9789664
Here age is pointing to different id upon changing henc int is immutable
booleans, floats, complex numbers are also immutable


Tuple is immutable so we get below error
message is immutable so we get below error
Traceback (most recent call last):
  File "/home/localadmin/PGB-2022/kranthi_PGB-2022/PYTHON/day1/MuiMu.py", line 30, in <module>
    tuple1[0] = 4
TypeError: 'tuple' object does not support item assignment
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
operations on list output:

['apple', 'banana', 'cherry', 'mango']
list after removing all elemnts using clear
[]
['apple', 'banana', 'cherry']
Occurrence of cherry in fruits list =  1


list extending list using l1.extend(l2)
['apple', 'banana', 'cherry', 'Ford', 'BMW', 'volvo']
Index of cherry :  2
List after inserting orange at 2 ['apple', 'banana', 'orange', 'cherry', 'Ford', 'BMW', 'volvo']
list after removing element at 2 and banana ,reversing the list
['volvo', 'BMW', 'Ford', 'cherry', 'apple']
cars list after sorting ['BMW', 'Ford', 'volvo']
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
operations on string output:

string converted to upper case:
WELCOME TO THE WORLD OF PROGRAMMING


String converted to lower case:
welcome to the world of programming


String Converted to title strating words are capital:)
Welcome To The World Of Programming
Number of times 'o' occured :  5


last character checking:
True
Since string contains " "  str.isalpha() returns false:
False
first charater of the string converted to capital:
Welcome to the world of programming
program to get position of a char in a string
the character p is present at 25
Reverse of string using slice:
gnimmargorp fo dlrow eht ot emoclew
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
operations on tuple out put:

(10, 20, 30, 40, 50, 10, 60, 10)
Occurrence of a specified value=10 in the tuple:
3
Enter number to find position50
the Number 50 is present at position 5
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
output:
dictionay with same value:
{1: 5, 2: 5, 3: 5}
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
opeerations on dictionary:

{1: 'hi', 2: 'kranthi', 3: 'welcome', 4: 'to python'}
 printing value of key:3 
welcome
removing the element with specified key: 1
{2: 'kranthi', 3: 'welcome', 4: 'to python'}
removing the last inserted key value pair:
{2: 'kranthi', 3: 'welcome'}
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
operations on set output:

{'t', 'n', 'a', 'k', 'r', 'i', 'h'}
Adding a element to set using myset.add():
{'t', 'n', 'a', 'k', 'r', 'i', 'y', 'h'}
Removing letter 't' element from the set
{'n', 'a', 'k', 'r', 'i', 'y', 'h'}
{1, 2, 3, 4}
{3, 4, 5, 6, 7, 8}
 elements in setx but not in sety
{1, 2}
set of elements common in both sets
{3, 4}
Return True if no items in set x is present in set y
False
Return True if all items in set x are present in set y
False
Return True if all items in set y are present in set x
False
Return a set that contains all items from both sets, except items that are present in both sets:
{1, 2, 5, 6, 7, 8}
Remove the items that are present in both sets, AND insert the items that is not present in both sets
{1, 2, 3, 4, 5, 6, 7, 8}
Return a set that contains all items from both sets, duplicates are excluded
{1, 2, 3, 4, 5, 6, 7, 8}
Insert the items from set y into set x
{1, 2, 3, 4, 5, 6, 7, 8}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
