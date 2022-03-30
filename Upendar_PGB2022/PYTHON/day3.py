# 1 Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class vechile:
    brand="bmw"
    def __init__(self,maximum_speed,mileage):
        self.maximum_speed=maximum_speed
        self.mileage=mileage
    def seating_capacity(self,capacity):
        return capacity
    def fare_charge(self):
        return self.capacity*100

sample_model=vechile(100,15)
print(sample_model.maximum_speed,sample_model.mileage)

class taxi(vechile):
    pass
taxi_object=taxi(60,18)
print(taxi_object.maximum_speed,taxi_object.mileage)

class bus(vechile):
    def seating_capacity(self,capacity=5):
        self.capacity=capacity
        return super().seating_capacity(capacity=5)
    def fare_charge(self):
        amount = super().fare_charge()
        amount += amount * 10 / 100
        return amount
bus_o=bus(120,16)
print(bus_o.seating_capacity())
print(taxi_object.brand)
print(bus_o.fare_charge())
##################################################################

# 6 Create a Time class and initialize it with hours and minutes.
class  Time(object):
    def __init__(self, hours, minutes):                  # declare hours,minutes
        self.hours = hours
        self.minutes = minutes
    def addTime(t1, t2):
        t3 = Time(0, 0)                                 # creating new object
        t3.hours = t1.hours + t2.hours                  # sum of hours
        t3.minutes = t1.minutes + t2.minutes            # sum of minutes
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        return t3

    def displayTime(self):
        print("Time is %d hours and %d minutes" %(self.hours, self.minutes))

    def displayMinutes(self):
        print((self.hours * 60) + self.minutes, "minutes")
a = Time(2, 50)
b = Time(1, 20)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinutes()
##################################################################
# 7 Create an iterator that returns numbers, starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations
class numbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = numbers()
myiter = iter(myclass)
for x in myiter:
  print(x)

##################################################################
# 8 write a Python class to get all possible unique subsets from a set of distinct integers
class uniquesubsets:
    def subset(self, set1):
        return self.subsetsRecur([], sorted(set1))

    def subsetsRecur(self, current, set1):
        if set1:
            return self.subsetsRecur(current, set1[1:]) + self.subsetsRecur(current + [set1[0]], set1[1:])
        return [current]
print(uniquesubsets().subset([4, 5, 6]))

##########################################################################
# 9 Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number
class py_1:
    def indices(self,nums,target):
        lookup={}
        for i ,num in enumerate(nums):
            if target-num in lookup:
                return (lookup[target-num],i)
            lookup[num]=i
print("index1=%d,index2=%d" %py_1().indices((10,20,10,40,50,60,70),50))

###########################################################################
# 10 Write a Python class to find the three elements that sum to zero from a set of n real numbers.
class py_solution:
 def threeSum(self, nums):
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

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

###########################################################################
# 11 Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also,
# check whether the said classes are subclasses of the built-in object class or not.
class student:
    pass
class marks:
    pass
student1=student()
marks1=marks()
print(isinstance(student1, student))
print(isinstance(marks1, student))
print(isinstance(marks1, marks))
print(isinstance(student1, marks))
print("check whether the said classes are subclasses of the built-in object class or not")
print(issubclass(student,object))
print(issubclass(marks,object))

###########################################################################
# 12  Write a Python program to sort a list of tuples using Lambda.
student2=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(student2)
student2.sort(key = lambda x: x[1])
print(student2)

###########################################################################
# 13 Write a Python program to sort a list of dictionaries by color using Lambda.
student3=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(student3)
student3.sort(key = lambda x: x['color'])
print(student3)

############################################################################
# 14 Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
def listofdicts(marks):
    result = map(dict,zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(marks)
print(listofdicts(marks))

############################################################################
# 15 Write a Python program to convert a given list of tuples to a list of strings using map function.

def listoftuple(fruits):
    result = list(map(' '.join, fruits))
    return list(result)
fruits=[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(fruits)
print(listoftuple(fruits))

############################################################################
# 16  Write a generator function which takes an integer n as a parameter.
        # The function should return a generator which counts down from n to 0. Test your function using a for loop.

def generator1(n):
    while n>=0:
        yield n
        n-=1
for i in generator1(10):
    print(i)
print()

############################################################################
# 17 Write an “abstract” class, Box, and use it to define some methods which any box object should have:
# 	a. add, for adding any number of items to the box,
# 	b. empty, for taking all the items out of the box and returning them as a list, and
# 	c. count, for counting the items which are currently in the box.
# 	d. Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects.
# 	e. Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.
from abc import ABC
class Box(ABC):
    def add():   pass
    def empty(): pass
    def count(): pass
class item(Box):
    def __init__(self,name,value):
        self.name=name
        self.value=value
class ListBox(Box):
    ans=[]
    def __init__(self):
        self.items=[]
    def add(self,*items):
        self.items.extend(items)
    def empty(self):
        self.ans=self.items.copy()
        self.items.clear()
        return self.ans
    def count(self):
        return len(self.ans)
class DictBox(Box):
    d={}
    def add(self,*items):
        for i in items:
            self.d[i.name]=i.value

    def empty(self):
        self.ans = self.d.copy()
        d = dict()
        return self.ans

    def count(self):
        return len(self.d)
lst=ListBox()
a=item("upendar",10)
b=item("rakesh",20)
c=item("varun",30)
lst.add(a,b,c)
ans=lst.empty()
for i in ans:
    print("Name is:",i.name,"Value is",i.value)
print("Count of list is:",lst.count())
dict1=DictBox()
dict1.add(a,b,c)
ans1=dict1.empty()
for key,items in ans1.items():
    print("Key is:",key, "Value is", items)









    def count(self):
        return len(self.items)

