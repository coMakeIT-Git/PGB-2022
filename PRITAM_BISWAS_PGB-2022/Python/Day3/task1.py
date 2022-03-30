"""
1. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
	a. Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class
	   and display it.
	b. Create a Car class that inherits from the Vehicle class.
	   Give the capacity argument of Bus.seating_capacity() a default value of 5
	c. Define a property that must have the same value for every class instance (object).
	d. Create a Bus child class that inherits from the Vehicle class.
	   The default fare charge of any vehicle is seating capacity * 100.
	If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
	So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
"""
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class vehcile:
    name="bmw"
    def __init__(self,maximum_speed,mileage):
        self.maximum_speed=maximum_speed
        self.mileage=mileage
    def seating_capacity(self,capacity):
        return capacity
    def fare_charge(self):
        return self.capacity*100

sa_vech=vehcile(100,15)
print("Vechicle speed and mileage :",sa_vech.maximum_speed,sa_vech.mileage)
#Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it.
class taxi(vehcile):
    pass
taxi_object=taxi(60,18)
print("Taxi speed and mileage :",taxi_object.maximum_speed,taxi_object.mileage)
#Create a Car class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 5
class bus(vehcile):
    def seating_capacity(self,capacity=5):
        self.capacity=capacity
        return super().seating_capacity(capacity=5)
    def fare_charge(self):
        amount = super().fare_charge()
        amount += amount * 10 / 100
        return amount
bus_o=bus(120,16)
print("Bus Capacity",bus_o.seating_capacity())
#Define a property that must have the same value for every class instance (object).
print("Brand Name:",bus_o.name)
#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
print("Bus fare charge :",bus_o.fare_charge())

"""
2. Create a Time class and initialize it with hours and minutes.
	a. Make a method addTime which should take two time object and add them. 
	   E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
	b. Make a method displayTime which should print the time.
	c. Make a method DisplayMinute which should display the total minutes in the Time. 
	   E.g.- (1 hr 2 min) should display 62 minute.
"""

class Time(object):
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def addTime(t1,t2):
        t3 = Time(0, 0)
        t3.hours = t1.hours + t2.hours
        t3.minutes = t1.minutes + t2.minutes
        while t3.minutes >=60:
            t3.hours +=1
            t3.minutes -=60
        return t3
    def displayTime(self):
        print("Time is %d hours and %d minutes" %(self.hours, self.minutes))
    def displayMinutes(self):
        print((self.hours * 60)+self.minutes, "minutes")
a=Time(2, 50)
b=Time(1, 20)
c=Time.addTime(a,b)
c.displayTime()
c.displayMinutes()



"""
3. Create an iterator that returns numbers, starting with 1, and each sequence will increase
   by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations

"""
print("Iterator:")
class Counter:
    def __init__(self, low, high):
        self.current = low -1
        self.high = high

    def __iter__(self):
        return self

    def __next__(self): # Python 2: def next(self)
        self.current += 1
        if self.current <= self.high:
            return self.current
        raise StopIteration

for c in Counter(1, 20):
    print(c)

"""
4. Write a Python class to get all possible unique subsets from a set of distinct integers. 
	Input : [4, 5, 6]
	Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
"""


class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]


print(py_solution().sub_sets([4, 5, 6]))

"""
5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
	Note: Do not use the same element twice.
	Input: numbers= [10,20,10,40,50,60,70], target=50
	Output: 3, 4
"""

class Elements:
  def Sum(self, nums, target):
       lookup = {}
       for i, num in enumerate(nums):
           if target - num in lookup:
               return (lookup[target - num], i )
           lookup[num] = i
print("index1: %d index2: %d" % Elements().Sum((10,20,10,40,50,60,70),50))

"""
6. Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
	Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
	Output : [[-10, 2, 8], [-7, -3, 10]]
"""
class python_class1:
 def sumofthree(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(python_class1().sumofthree([-25, -10, -7, -3, 2, 4, 8, 10]))

"""
7. Write a Python program to crate two empty classes, Student and Marks.
 Now create some instances and check whether they are instances of the said classes or not.
  Also, check whether the said classes are subclasses of the built-in object class or not.

"""

class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))

"""
8. Write a Python program to sort a list of tuples using Lambda.
	Original list of tuples:
	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
	Sorting the List of Tuples:
	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
tup=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

tup.sort(key=lambda x:x[1])
print("sort: ",tup)

"""
9. Write a Python program to sort a list of dictionaries by color using Lambda.
	Original list of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
	Sorting the List of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""
device_models = [{'make':'Asus', 'model':216, 'color':'Black'}, {'make':'NOKIA', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(device_models)
# to sort a list of dictionaries using Lambda
sorted_models = sorted(device_models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)

"""
10. Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
	Original dictionary of lists:
	{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
	Split said dictionary of lists into list of dictionaries:	
	[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language':80}]
"""
def dictionarylist(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Original dictionary of lists:")
print(marks)
print("\nSplit said dictionary of lists into list of dictionaries:")
print(dictionarylist(marks))
"""
11. Write a Python program to convert a given list of tuples to a list of strings using map function.
    Original list of tuples:
    [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
	
    Convert the said list of tuples to a list of strings:
    ['red pink', 'white black', 'orange green']
"""
def tuples_to_list(lst):
    result = list(map(' '.join, lst))
    return result
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples:")
print(colors)
print("\nConverting the current list of tuples to a list of strings:")
print(tuples_to_list(colors))
names = [('Sheridan','Gentry'), ('Laila','Mckee'), ('Ahsan','Rivas'), ('Conna','Gonzalez')]
print("\nOriginal list of tuples:")
print(names)
print("\nConverting the current list of tuples to a list of strings:")
print(tuples_to_list(names))
"""
12. Write a generator function which takes an integer n as a parameter. 
The function should return a generator which counts down from n to 0. Test your function using a for loop.
"""
print("Generator: ")
def generatorfun(n):
    while n>=0:
        yield n
        n-=1
for i in generatorfun(10):
    print(i)
print()
"""
17. Write an “abstract” class, Box, and use it to define some methods which any box object should have: 
	a. add, for adding any number of items to the box, 
	b. empty, for taking all the items out of the box and returning them as a list, and 
	c. count, for counting the items which are currently in the box. 
	d. Write a simple Item class which has a name attribute and a value attribute – you can 
	   assume that all the items you will use will be Item objects. 
	e. Now write two subclasses of Box which use different underlying collections to store items: 
	   ListBox should use a list, and DictBox should use a dict.
"""
class Box:
    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def add(self, *items):
        raise NotImplementedError()


class Item:
    def __init__(self, name, value):
        self.value = value
        self.name = name


class ListBox(Box):
    def __init__(self):
        self._items = []

    def empty(self):
        items = self._items
        self._items = []
        return items

    def displayItems(self):
        if self.count() == 0:
            print("No Items Found")
            return
        print("Item Attributes : ")
        for i in self._items:
            print(f"Name : {i.name}, Value : {i.value}")
        return

    def count(self):
        return len(self._items)

    def add(self, *items):
        self._items.extend(items)


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def displayItems(self):
        if self.count() == 0:
            print("No Items Found")
            return
        print("Item Attributes : ")
        for k, v in self._items.items():
            print(f"Name : {k}, Value : {v}")
        return

    def count(self):
        return len(self._items)

    def add(self, *items):
        self._items.update(dict((i.name, i.value) for i in items))


i1 = Item("Red", 1)
i2 = Item("Blue", 2)
i3 = Item("Green", 3)
i4 = Item("Yellow", 4)
i5 = Item("Black", 5)
print("List Box\n")
ObjListBox = ListBox()
ObjListBox.add(i1, i2, i3)
ObjListBox.displayItems()
ObjListBox.empty()
ObjListBox.displayItems()
print("\n\nDictionary Box\n")
ObjDictBox = DictBox()
ObjDictBox.add(i4, i5)
ObjDictBox.displayItems()
ObjDictBox.empty()
ObjDictBox.displayItems()
