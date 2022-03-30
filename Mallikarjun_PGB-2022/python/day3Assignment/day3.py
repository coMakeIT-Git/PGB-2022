
#1- Write a Python program to create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    color = "White"
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self, capacity):
        return capacity
    def fare(self):
        return self.capacity * 100
Bmw = Vehicle(340, 6)
print("Speed:", Bmw.max_speed, "Mileage:", Bmw.mileage)
######################################################################
#a- Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it
class Taxi(Vehicle):
    pass
Taxi = Vehicle(180, 18)
print("Speed:", Taxi.max_speed, "Mileage:", Taxi.mileage)
########################################################################
#b,d- Create a Car class that inherits from the Vehicle class. Give the capacity argument of
# Bus.seating_capacity() a default value of 5
class Car(Vehicle):
    def seating_capacity(self,capacity=5):
        self.capacity=capacity
        return super().seating_capacity(capacity)
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount
obj=Car(120,34)
print("The seating capacity of a Car is ", obj.seating_capacity())
print("Total Taxi fare is:", obj.fare())

##########################################################################

#c- Define a property that must have the same value for every class instance (object).

class Vehicle:
    color = "White"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bmw(Vehicle):
    pass

class Taxi(Vehicle):
    pass

Bmw = Vehicle(340, 6)
print("BMW-","Color:",Bmw.color, "Speed:",Bmw.max_speed, "Mileage:",Bmw.mileage)

Taxi = Vehicle(180, 18)
print("Taxi-","Color:",Taxi.color,"Speed:", Taxi.max_speed, "Mileage:", Taxi.mileage)

#################################################################################

#6- Create a Time class and initialize it with hours and minutes


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
a=Time(3, 40)
b=Time(1, 30)
c=Time.addTime(a,b)
c.displayTime()
c.displayMinutes()

##################################################################################

#7- Create an iterator that returns numbers, starting with 1, and each
# sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations


class Iterator:
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

value = Iterator()
myiterator = iter(value)

for x in myiterator:
  print(x)


#######################################################################

#8- Write a Python class to get all possible unique subsets from a set of distinct integers

class Subsets:
    def sub_sets(self, set):
        return self.subsetsRecur([], sorted(set))

    def subsetsRecur(self, current, set):
        if set:
            return self.subsetsRecur(current, set[1:]) + self.subsetsRecur(current + [set[0]], set[1:])
        return [current]


print(Subsets().sub_sets([4, 5, 6]))

#######################################################################

#9-  Write a Python class to find a pair of elements (indices of the two numbers)
# from a given array whose sum equals a specific target number

class pair_of_elements:
  def twoSum(self, numbers, target):
       lookup = {}
       for i, num in enumerate(numbers):
           if target - num in lookup:
               return (lookup[target - num], i )
           lookup[num] = i
print("index1=%d, index2=%d" % pair_of_elements().twoSum((10,20,30,50,60,70),50))


#########################################################################################

#10- Write a Python class to find the three elements that sum to zero from a set of n real numbers


class elements:
 def threeSum(self, num):
        num, result, i = sorted(num), [], 0
        while i < len(num) - 2:
            j, k = i + 1, len(num) - 1
            while j < k:
                if num[i] + num[j] + num[k] < 0:
                    j += 1
                elif num[i] + num[j] + num[k] > 0:
                    k -= 1
                else:
                    result.append([num[i], num[j], num[k]])
                    j, k = j + 1, k - 1
                    while j < k and num[j] == num[j - 1]:
                        j += 1
                    while j < k and num[k] == num[k + 1]:
                        k -= 1
            i += 1
            while i < len(num) - 2 and num[i] == num[i - 1]:
                i += 1
        return result

print(elements().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


###########################################################################

#11-crate two empty classes, Student and Marks. Now create some instances and
# check whether they are instances of the said classes or not. Also, check whether
# the said classes are subclasses of the built-in object class or not

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

###############################################################################################

#12- Write a Python program to sort a list of tuples using Lambda

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)


########################################################################################

#13- Write a Python program to sort a list of dictionaries by color using Lambda

models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)


#####################################################################################

#14- Write a Python program to split a given dictionary of lists into list of dictionaries using map function

def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Original dictionary of lists:")
print(marks)
print("\nSplit list of dictionaries:")
print(list_of_dicts(marks))


################################################################################

#15- Write a Python program to convert a given list of tuples to a list of strings using map function

def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples:")
print(colors)
print("\nConvert list of tuples:")
print(tuples_to_list_string(colors))


###########################################################################################

#16- Write a generator function which takes an integer n as a parameter.
# The function should return a generator which counts down from n to 0. Test your function using a for loop


def generator(n):
    while n>=0:
        yield n
        n-=1
for i in generator(5):
    print(i)



###########################################################################################

#17- Write an “abstract” class, Box, and use it to define some methods which any box object should have:
	#a. add, for adding any number of items to the box,
	#b. empty, for taking all the items out of the box and returning them as a list, and
	#c. count, for counting the items which are currently in the box.
	#d. Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects.
	#e. Now write two subclasses of Box which use different underlying collections to
        #store items: ListBox should use a list, and DictBox should use a dict


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
a=item("Malliakarjun",10)
b=item("Vinay",20)
c=item("Aadithya",30)
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