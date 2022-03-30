out put for vehicle

The seating capacity of a school bus is 40 passengers
Fare collected by the bus is:
4040.0
taxi name is: skycabs
taxi maximaum speed is 100
taxi mileage is 18
---------------------------------------------------------------------------------------------------------------------------------------

Sum of times:
4 10
The time is 4 hours and 10 mins
total minutes are 250
---------------------------------------------------------------------------------------------------------------------------------------

a Python class to get all possible unique subsets from a set of distinct integers.
[[], [4], [4, 5], [5], [4, 5, 6], [5, 6], [6]]

---------------------------------------------------------------------------------------------------------------------------------------

 Indices of elements whose sum is target value:
(0, 4)
---------------------------------------------------------------------------------------------------------------------------------------

Triplets Whose sum is equal to zero:
[-3, 1, 2]
[-1, 0, 1]

---------------------------------------------------------------------------------------------------------------------------------------

Tells wether stu1 is a instance of student or not :
True
Tells wether mark is a instance of marks class or not :
True
Tells wether stu1 is a instance of marks or not :
False
student is a subclass of object or not:
True
marks is a subclass of object or not:
True
---------------------------------------------------------------------------------------------------------------------------------------
sorting list of tuples:
Sorting using Lambda expression:
Original list of tuples:
[('kranthi', 21), ('raju', 20), ('manasa', 18), ('Swetha', 15)]

Sorting the List of Tuples:
[('Swetha', 15), ('manasa', 18), ('raju', 20), ('kranthi', 21)]

---------------------------------------------------------------------------------------------------------------------------------------
Originalist:
[{'make': 'Nokia', 'model': 216, 'color': 'Yellow'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorted list with respect to color:
[{'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Nokia', 'model': 216, 'color': 'Yellow'}]
---------------------------------------------------------------------------------------------------------------------------------------

Original list of tuples:
[('red', 'pink'), ('white', 'black'), ('orange', 'green')]

Convert the said list of tuples to a list of strings:
['red pink', 'white black', 'orange green']
---------------------------------------------------------------------------------------------------------------------------------------

generator out put:
Printing numbers generated using generator with  for loop:
10
9
8
7
6
5
4
3
2
1

---------------------------------------------------------------------------------------------------------------------------------------

class Box():
    def add(self,*tems):
        pass
    def empty(self):
        pass
    def count(self):
        pass
class Item():
    def __init__(self,name,value):
        self.name=name
        self.value = value
class ListBox(Box):
    def __init__(self):
        self._items = []
    def add(self,*items):
        self._items=_items.extend(items)
    def empty(self):
        items=self._items
        self._items=[]
        return items

    def count(self):
        return len(self._items)

class DictBox(Box):
    def __init__(self,_items):
        self._items={}
    def add(self,*items):
       _items.update(dict((i.name,i)for i in items ))
    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items
    def count(self):
        return len(self._items)
---------------------------------------------------------------------------------------------------------------------------------------





