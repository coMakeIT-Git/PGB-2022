#Task 1:
class vehicle:
    color = "Black"
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return capacity

    def fare(self):
        return self.capacity * 100

model1 = vehicle("GLS", 220, 20, 5)
print("Name of the car:", model1.name)
print("Max speed of car:", model1.max_speed)
print("Mileage of the car:", model1.mileage)
print("Capacity: ", model1.capacity)
print(model1.color)
#a
class taxi(vehicle):
    pass
zoom_cabs = taxi("Alturas", 200, 14, 7)
print("Taxi name: ", zoom_cabs.name, "Top speed: ", zoom_cabs.max_speed, "Mileage: ",zoom_cabs.mileage, zoom_cabs.color)
print("Capacity: ", zoom_cabs.capacity)
#b
class car(vehicle):
    def seating_capacity(self, capacity=5):
        return super().seating_capacity(capacity=5)
super_car = car("porshe", 280, 6, 2)
print(super_car.seating_capacity())
print(super_car.color)
#d
class bus(vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

school_bus = bus("Marcopolo", 100, 4, 35)
print("Total fare of the bus is: ", school_bus.fare())

#Task 2:
class Time:
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins
    def addTime(time1, time2):
        time3 = Time(0, 0)
        if time1.mins + time2.mins > 60:
            time3.hours = (time1.mins + time2.mins)/60
        time3.hours = time3.hours + time2.hours + time1.hours
        time3.mins = (time1.mins + time2.mins) - (((time1.mins + time2.mins) / 60) * 60)
        return time3
    def displayTime(self):
        print("Time is",self.hours, "hours and ", self.mins, "minutes")
    def DisplayMinute(self):
        print((self.hours * 60) + self.mins)

a = Time(2, 50)
b = Time(1,20)
c = Time.addTime(a, b)
c.displayTime()
c.DisplayMinute()

#Task 3:
class iterativeNumbers:
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

myclass = iterativeNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)

#Task 4:
class uniqueSubsets:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]
print(uniqueSubsets().sub_sets([1,2,3]))

#Task 5:
class pair_of_elements:
    def specific_sum(self, arr, targetSum):
        sum = {}
        for i, arr in enumerate(arr):
            if targetSum - arr in sum:
                return (sum[targetSum - arr], i)
            sum[arr] = i
print("index of 1st element = %d, index of second element = %d" % pair_of_elements().specific_sum((10, 20, 10, 40, 50, 60, 70), 50))

#Task 6:
class SumToZero:
 def sum_of_three(self, array):
        array, result, i = sorted(array), [], 0
        while i < len(array) - 2:
            j, k = i + 1, len(array) - 1
            while j < k:
                if array[i] + array[j] + array[k] < 0:
                    j += 1
                elif array[i] + array[j] + array[k] > 0:
                    k -= 1
                else:
                    result.append([array[i], array[j], array[k]])
                    j, k = j + 1, k - 1
                    while j < k and array[j] == array[j - 1]:
                        j += 1
                    while j < k and array[k] == array[k + 1]:
                        k -= 1
            i += 1
            while i < len(array) - 2 and array[i] == array[i - 1]:
                i += 1
        return result

print(SumToZero().sum_of_three([-25, -10, -7, -3, 2, 4, 8, 10]))

#Task 7:
class Student:
    pass
class Marks:
    pass
stud = Student()
score = Marks()
print("Checking whether the stud and score instances are the instances of Students and Marks class respectively or not")
print(isinstance(stud, Student))
print(isinstance(score, Student))
print(isinstance(stud, Marks))
print(isinstance(score, Marks))
print("checking whether the said classes are subclasses of the built-in object class or not")
print(issubclass(Student,object))
print(issubclass(Marks,object))

#Task 8:
max_speed_of_cars = [("Audi", 220),("Mercedes", 261),("BMW", 289),("Volvo", 200)]
print("Original list before sorting: ")
print(max_speed_of_cars)
max_speed_of_cars.sort(key = lambda x : x[1])
print("List of tuples after sorting:")
print(max_speed_of_cars)

#Task 9:
bikes = [{'make':'Harley','model':2017,'color':'black'},{'make':'Honda','model':2022,'color':'orange'},{'make':'Bajaj','model':2020,'color':'grey'},{'make':'Triumph','model':2019,'color':'red'}]
print("List of dictionaries before sorting:")
print(bikes)
super_bikes = sorted(bikes, key = lambda y : y['color'])
print("List of dictionaries after sorting:")
print(super_bikes)
super_bikes1 = sorted(bikes, key = lambda p : p['model'])
print("List of dictionaries sorting based on the year of manufacturing:")
print(super_bikes1)

#Task 10:
def list_of_dictionaries(bmi):
    converted_list = map(dict, zip(*[[(key, v) for v in value] for key, value in bmi.items()]))
    return list(converted_list)

bmi = {'Age':[22, 47, 38, 55, 18],'Height':[182,150,161,145,137]}
print("Dictionary of lists before splitting:")
print(bmi)
print("Converting dictionary of lists into list of dictionaries:")
print(list_of_dictionaries(bmi))

#Task 11:
def tup_to_list_of_string(brands):
    converted_tup_to_string = list(map(' '.join, brands))
    return converted_tup_to_string

automotives = [("Mahindra","Thar"),("volvo","S90"),("Mercedes","Gwagon")]
print("List of tuples:")
print(automotives)
print("Converting list of tuples into list of strings:")
print(tup_to_list_of_string(automotives))

#Task 12:
def my_generator(n):
    while n>=0:
        yield n
        n -= 1
print("Printing numbers from n to 0 using Generator function:")
for i in my_generator(20):
    print(i)

#Task 13:
from abc import ABC
class Box(ABC):
    def add(self):
        pass
    def empty(self):
        pass
    def count(self):
        pass
class Item(Box):
    def __init__(self, name, value):
        self.name = name
        self.value = value
class ListBox(Box):
    ans = []
    def __init__(self):
        self.items = []
    def add(self, *items):
        self.items.extend(items)
    def empty(self):
        self.ans = self.items.copy()
        self.items.clear()
        return self.ans
    def count(self):
        return len(self.ans)
class DictBox(Box):
    d = {}
    def add(self, *items):
        for i in items:
            self.d[i.name] = i.value
    def empty(self):
        self.ans = self.d.copy()
        d = dict()
        return self.ans
    def count(self):
        return len(self.d)
lst = ListBox()
abstr_cl1 = Item("Ram",10)
abstr_cl2 = Item("Harish",20)
abstr_cl3 = Item("Girish",30)
lst.add(abstr_cl1,abstr_cl2,abstr_cl3)
ans = lst.empty()
for i in ans:
    print("Name: ", i.name, "Age: ", i.value)
print("Count of list is: ",lst.count())
dict1 = DictBox()
dict1.add(abstr_cl1,abstr_cl2,abstr_cl3)
ans1 = dict1.empty()
for key, items in ans1.items():
    print("Key:",key,"Value:",items)
