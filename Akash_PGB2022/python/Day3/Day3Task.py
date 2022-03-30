# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
# Define a property that must have the same value for every class instance (object).
    brand = "Ferrari"
    def __init__(self, max_speed, mileage,capacity=5):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity*100
print("**********")
# Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it.
class Taxi(Vehicle):
    pass
modelX = Vehicle(300, 20)
print("Max spped is:",modelX.max_speed, "mileage is:",modelX.mileage)

#Create a Car class that inherits from the Vehicle class
class Car(Vehicle):
    def seating_capacity(self, capacity=5):
        print("seating capacity:",capacity)
print("**********")


# Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
class Bus(Vehicle):
    def fare(self):
        total_amount = super().fare()
        total_amount=total_amount+total_amount*(10/100)
        return total_amount
bus_obj = Bus(100,14,8)
print("max speed:{},mileage:{},capacity:{}".format(bus_obj.max_speed,bus_obj.mileage,bus_obj.capacity))
print("Total fare to paasengers:", bus_obj.fare())
print("**********")

#Create a Time class and initialize it with hours and minutes.
#a. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
class Time():
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def addtime(t1,t2):
        t3=Time(0,0)
        if t1.minutes + t2.minutes > 60:
            t3.hours = (t1.minutes + t2.minutes) // 60
        t3.hours = t3.hours + t1.hours + t2.hours
        t3.minutes = (t1.minutes + t2.minutes) % 60
        return t3
    def displaytime(self):
        print("Time is {} Hours And {} Minutes".format(self.hours,self.minutes))
    def displayminutes(self):
        print("Total Minutes:",(self.hours*60)+self.minutes)
time_obj1=Time(2,3)
time_obj2=Time(4,5)
time_obj3=Time.addtime(time_obj1,time_obj2)
time_obj3.displaytime()
time_obj3.displayminutes()
print("**********")


#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations
class Iterator:
    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        if self.number<=20:
            number = self.number
            self.number += 1
            return number
        else:
            raise StopIteration
itr_list = Iterator()
itr_obj = iter(itr_list)
for num in itr_obj:
    print(num)
print("**********")


# Write a Python class to get all possible unique subsets from a set of distinct integers.
#	Input : [4, 5, 6]
#Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
class unique_sets:
    def sub_sets(self, s_set):
        return self.subsets([], sorted(s_set))

    def subsets(self, current, s_set):
        if s_set:
            return self.subsets(current, s_set[1:]) + self.subsets(current + [s_set[0]], s_set[1:])
        return [current]
print(unique_sets().sub_sets([4, 5, 6]))
print("**********")


#Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
#Note: Do not use the same element twice.
#Input: numbers= [10,20,10,40,50,60,70], target=50
#Output: 3, 4
class pair_elements:
    def summ(self,nums,total):
        b={}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==total:
                    b[nums[i]]=i+1
        return b
pair_elements_obj=pair_elements()
summ_obj=pair_elements_obj.summ([10,20,10,40,50,60,70],50)
for i,j in summ_obj.items():
    print(j)
print("**********")


# Write a Python class to find the three elements that sum to zero from a set of n real numbers.
#Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
#Output : [[-10, 2, 8], [-7, -3, 10]]
class real_numbers:
    def pairs(self,lst):
        b=[]
        for i in lst:
            for j in lst:
                for k in lst:
                    c = []
                    if(i+j+k==0):
                        c=c+[i]+[j]+[k]
                        c=sorted(c)
                        b.append(c)
        d=[]
        for i in b:
            if i not in d:
                d.append(i)
        return d
new_list = real_numbers().pairs( [-25, -10, -7, -3, 2, 4, 8, 10])
print(new_list)
print("**********")


# Write a Python program to crate two empty classes, Student and Marks.
# Now create some instances and check whether they are instances of the said classes or not.
# Also, check whether the said classes are subclasses of the built-in object class or not.

class Teacher:
    pass
class Student:
    pass
teacher=Teacher()
student=Student()
print(isinstance(student, Student))
print(isinstance(teacher, Teacher))
print(isinstance(student, Teacher))
print(isinstance(teacher, Student))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Teacher, object))
print("**********")


# Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples:
#[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#Sorting the List of Tuples:
#[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths',

marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
marks.sort(key=lambda x:x[1])
print(marks)
print("**********")


# Write a Python program to sort a list of dictionaries by color using Lambda.
#Original list of dictionaries :
#[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#Sorting the List of dictionaries :
#[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
dict.sort(key=lambda x:x["color"])
print(dict)
print("**********")


#Write a Python program to convert a given list of tuples to a list of strings using map function.
#Original list of tuples:
#[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
def combine(n):
    res = list(map(' '.join,n))
    return res
s = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(combine(s))
print("**********")


#Write a generator function which takes an integer n as a parameter.
# The function should return a generator which counts down from n to 0. Test your function using a for loop.

def count_down(num):
    n=num
    while n>0:
        yield n
        n=n-1
x=count_down(10)
for i in x:
    print(i)
print("**********")


#Write an “abstract” class, Box, and use it to define some methods which any box object should have:
#a. add, for adding any number of items to the box,
#b. empty, for taking all the items out of the box and returning them as a list, and
#c. count, for counting the items which are currently in the box.
#d. Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects.
#e. Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.






