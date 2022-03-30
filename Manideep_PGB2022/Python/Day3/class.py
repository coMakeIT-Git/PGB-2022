
from itertools import *
from abc import ABC, abstractmethod
 
# 1. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
# 	a. Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it.
# 	b. Create a Car class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 5
# 	c. Define a property that must have the same value for every class instance (object).
# 	d. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add 
#     an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self,s,m):
        self.maxspeed=s
        self.mileage=m
        self.capacity=5
    def display(self):
        return ' Maxspeed is {}\n mileage is {}'.format(self.maxspeed,self.mileage)
    def seating_capacity(self,capacity):
        self.capacity=capacity
        return f"The seating capacity for vehicle is {capacity}"
    def fare(self):
        return self.capacity*100
taxi=Vehicle(66,50)

print(taxi.display())

class car(Vehicle):
    gears=5
    def seating_capacity(self,capacity=5):
        return super().seating_capacity(capacity)

c=car(160,30)
d=car(12,120)
print(c.seating_capacity()) 
print(c.gears,d.gears)

class Bus(Vehicle):
    def fare(s):
        defaultfare = super().fare()
        amount =defaultfare+ defaultfare * 10 / 100
        return amount
bus = Bus(67, 50)
print("Total Bus fare is:", bus.fare())




# Create a Time class and initialize it with hours and minutes.
# 	a. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 	b. Make a method displayTime which should print the time.
# 	c. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.



class Time:
    def __init__(self,hr,min):
        self.hour=hr
        self.minutes=min
    def addTime(t1,t2):
        T=Time(0,0)
        if t1.minutes+t2.minutes > 60:
            T.hour = (t1.minutes+t2.minutes)//60
        T.hour = T.hour+t1.hour+t2.hour
        T.minutes = (t1.minutes+t2.minutes)%60
        return T
        
    def displayTime(self):
        return 'hours is {} minutes is {}'.format(self.hour,self.minutes)
    def DisplayMinute(self):
        return 'minutes is {}'.format(self.hour*60+self.minutes)

t1=Time(2,50)
t2=Time(1,20)
t3=Time.addTime(t1,t2)
print(t3.displayTime())
print(t3.DisplayMinute())


# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations
class generate:
  def __iter__(self):
    self.s = 1
    return self

  def __next__(self):
    if self.s <= 20:
      x = self.s
      self.s += 1
      return x
    else:
      raise StopIteration

o = generate()
Iter = iter(o)

for x in Iter:
  print(x)

# Write a Python class to get all possible unique subsets from a set of distinct integers. 
# 	Input : [4, 5, 6]
# 	Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]


class subsets:
    def __init__(s,l):
        s.l=l
    def getsubsets(s):
        L=[]
        for i in range(2**len(s.l)):
            k=[]
            for j in range(i):
                if (1<<j)&i:
                    k.append(s.l[j])
            L.append(k)
        return L
a=subsets([4,5,6])
print(a.getsubsets())


# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
# 	Note: Do not use the same element twice.
# 	Input: numbers= [10,20,10,40,50,60,70], target=50
# 	Output: 3, 4

class findpair:
    def __init__(self,l):
        self.t=l
    def getpairs(self,t):
        for i in range(len(self.t)):
            for j in range(i+1,len(self.t)):
                if self.t[i]!=self.t[j] and self.t[i]+self.t[j]==t:
                        print(i+1,j+1)
        return (-1,-1)
n=[10,20,10,40,50,60,70]
p=findpair(n)
p.getpairs(50)

# Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
# 	Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# 	Output : [[-10, 2, 8], [-7, -3, 10]]

class findzersum:
    def __init__(self,l):
        self.l=l
    def get(self):
        self.l.sort()
        k=[]
        for i in range(len(self.l)-2):
            t=-(self.l[i])
            p=i+1
            q=len(self.l)-1
            while p<q:
                if self.l[p]+self.l[q]==t:
                    k.append([-t,self.l[p],self.l[q]])
                    p+=1
                    q-=1
                elif self.l[p]+self.l[q]<t:
                    p+=1
                else:
                    q-=1
        return k
t=findzersum([-25, -10, -7, -3, 2, 4, 8, 10])
print(t.get())
        
# Write a Python program to crate two empty classes, Student and Marks. Now create some instances and 
# check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.
class Student:
    pass
class Marks:
    pass
s1=Student()
s2=Student()
m1=Marks()
m2=Marks()
print(isinstance(s1,Student))
print(isinstance(m2,Student))
print(isinstance(m1,Student))
print(isinstance(s2,Student))
print(issubclass(Student, object))
print(issubclass(Marks, object))

# Write a Python program to sort a list of tuples using Lambda.
# 	Original list of tuples:
# 	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# 	Sorting the List of Tuples:
# 	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

l=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
l.sort(key=lambda f:f[1])
print(l)

# Write a Python program to sort a list of dictionaries by color using Lambda.
# 	Original list of dictionaries :
# 	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# 	Sorting the List of dictionaries :
# 	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

s=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
s.sort(key=lambda f:f['color'])
print(s)

# Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
# 	Original dictionary of lists:
# 	{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# 	Split said dictionary of lists into list of dictionaries:	
# 	[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language':80}]
d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
l=list(map(dict, zip(*[[(key, val) for val in value] for key, value in d.items()])))
print(l)

#  Write a Python program to convert a given list of tuples to a list of strings using map function.
# 	Original list of tuples:
# 	[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
	
# 	Convert the said list of tuples to a list of strings:
# 	['red pink', 'white black', 'orange green']
a=[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
def get(a):
    return ''.join(a)
l=list(map(get,a))
print(l)
# Write a generator function which takes an integer n as a parameter. 
# The function should return a generator which counts down from n to 0. Test your function using a for loop.

def gen(n):
    while n>=0:
        yield n
        n-=1
for i in gen(10):
    print(i)
print()

# Write an “abstract” class, Box, and use it to define some methods which any box object should have: 
# 	a. add, for adding any number of items to the box, 
# 	b. empty, for taking all the items out of the box and returning them as a list, and 
# 	c. count, for counting the items which are currently in the box. 
# 	d. Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects. 
# 	e. Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.

class Box:
    def add(self, *items):
        pass
    def empty(self):
        pass

    def count(self):
        pass


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *i):
        self._items.extend(i)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *i):
        self._items.update(dict((i.name, i) for i in i))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)