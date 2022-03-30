#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    #Define a property that must have the same value for every class instance (object).
    brand="BMW"
    def __init__(self,max_speed,mileage,capacity=5):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity=capacity
    def fare(self):
        return self.capacity*100

#a. Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it.
class Taxi(Vehicle):
    pass

taxi_obj=Taxi(120,15)
print("taxi details: max speed:{} and mileage:{}".format(taxi_obj.max_speed,taxi_obj.mileage))

#Create a Car class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 5
class Car(Vehicle):
    def seating_capacity(self,capacity=5):
        print("seating capacity:",capacity)

#Create a Bus child class that inherits from the Vehicle class
class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        total_amount = amount + amount * (10 / 100)
        return total_amount
bus_obj=Bus(100,12,6)
print("bus details: max speed:{},mileage:{},capacity:{}".format(bus_obj.max_speed,bus_obj.mileage,bus_obj.capacity))
print("total fare to passengers: RS",bus_obj.fare())
print("################")

#Create a Time class and initialize it with hours and minutes.
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
        print("time is {} hours and {} minutes".format(self.hours,self.minutes))
    def displayminutes(self):
        print("total minutes:",(self.hours*60)+self.minutes)
time_obj1=Time(2,3)
time_obj2=Time(4,5)
time_obj3=Time.addtime(time_obj1,time_obj2)
time_obj3.displaytime()
time_obj3.displayminutes()
print("###########")

#Create an iterator that returns numbers, starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations
class Iterator:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num<=20:
            num=self.num
            self.num =self.num+1
            return num
        else:
            raise StopIteration
a=Iterator()
b=iter(a)
for x in b:
    print(x)
print("#############")

#Write a Python class to get all possible unique subsets from a set of distinct integers.
	#Input : [4, 5, 6]
	#Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

class unique_subsets:
    def sub_sets(self,sett):
        return self.subsets_recur([],sorted(sett))

    def subsets_recur(self,curr,sett):
        if sett:
            return self.subsets_recur(curr,sett[1:]) + self.subsets_recur(curr +[sett[0]],sett[1:])
        return [curr]
print(unique_subsets().sub_sets([7,2,6]))
print("########")

#Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
	#Note: Do not use the same element twice.
	#Input: numbers= [10,20,10,40,50,60,70], target=50
	#Output: 3, 4

class pair_elements:
    def summ(self,nums,total):
        b={}
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x]+nums[y]==total:
                    b[nums[x]]=x+1
        return b
pair_elements_obj=pair_elements()
summ_obj=pair_elements_obj.summ([10,20,10,40,50,60,70],50)
for x,y in summ_obj.items():
    print(y)
print("############")
#Write a Python class to find the three elements that sum to zero from a set of n real numbers.
	#Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
	#Output : [[-10, 2, 8], [-7, -3, 10]]

class real_nums:
    def pairs(self,lst):
        b=[]
        for x in lst:
            for y in lst:
                for z in lst:
                    c = []
                    if(x+y+z==0):
                        c=c+[x]+[y]+[z]
                        c=sorted(c)
                        b.append(c)
        d=[]
        for x in b:
            if x not in d:
                d.append(x)
        return d
obj=real_nums().pairs( [-25, -10, -7, -3, 2, 4, 8, 10])
print(obj)
print("#########")

#Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not.
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
print("##########")













