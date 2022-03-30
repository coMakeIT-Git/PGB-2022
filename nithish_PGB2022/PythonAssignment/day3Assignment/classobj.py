#class, objects, inheritance, overide

class Vehcile:
    brand="TATA"
    def __init__(self,maxspeed,mileage,capacity):
        self.maxspeed=maxspeed
        self.mileage=mileage
        self.capacity=capacity

    def display(self):
        print("maxspeed:",self.maxspeed," mileage:",self.mileage," capacity:",self.capacity," brand:",self.brand)

    def seating_capacity(self):
        print("seating capacity:",self.capacity)

    def fair(self):
        print("fair charge:",self.capacity*100)

class Car(Vehcile):
    def __init__(self,maxspeed,mileage,capacity=5):
        super().__init__(maxspeed,mileage,capacity)

class Taxi(Vehcile):
    pass

class Bus(Vehcile):
    def fair(self):
        print("fair charge:",self.capacity*100+(self.capacity*100)*0.1)

print("Taxi")
taxi=Taxi(115,20,4)
taxi.display()
taxi.fair()
print()

print("Bus")
bus=Bus(100,13,45)
bus.seating_capacity()
bus.display()
bus.fair()

print("Car")
car=Car(140,22)
car.display()
car.seating_capacity()
print()


#-----------------------------------------------------------------------------------------------------------------------


class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def addTime(time1,time2):
        time3=Time(0,0)
        time3.hours=time1.hours+time2.hours
        time3.minutes=time1.minutes+time2.minutes
        while(time3.minutes>=60):
            time3.hours+=1
            time3.minutes=time3.minutes-60
        return time3
    def displayTime(self):
        print("The Time is",self.hours,"hours and",self.minutes,"minutes")
    def displayMinute(self):
        minute=0
        if(self.hours>=1):
            minute+=60
            self.hours-=1
        minute+=self.minutes
        print("Total minutes in the time are:",minute)

obj1=Time(2,50)
obj2=Time(1,20)
timeobj=Time.addTime(obj1,obj2)
timeobj.displayTime()
timeobj.displayMinute()
print()

#-----------------------------------------------------------------------------------------------------------------------
#Python class to find the three elements that sum to zero from a set of n real numbers.

class Threesum:
    def zerosum(self,list):
        list=sorted(list)
        r=[]
        i=0
        while i < len(list)-2:
            j=i+1
            k=len(list)-1
            while j < k:
                if list[i]+list[j]+list[k] < 0:
                    j+=1
                elif list[i]+list[j]+list[k] > 0:
                    k-=1
                else:
                    r.append([list[i],list[j],list[k]])
                    j=j+1
                    k=k-1
                    while j < k and list[j]==list[j-1]:
                        j+=1
                    while j < k and list[k]==list[k+1]:
                        k-=1
            i+=1
            while i < len(list)-2 and list[i]==list[i-1]:
                i+=1
        return r

list=[-25,-10,-7,-3,2,4,8,10]
threesum=Threesum()
print("set of three elements sum=0:",threesum.zerosum(list))
print()

#-----------------------------------------------------------------------------------------------------------------------
#array whose sum equals a specific target number

def check():
	l=[20,25,32,4,2,5]
	n=[]
	target=6
	for i in l:
		n.append(target-i)
	for i in range(0,len(n)):
		if n[i] in l:
			return i,l.index(n[i])
	return -1,-1

print(check())
print()

#-----------------------------------------------------------------------------------------------------------------------
#function should return a generator which counts down from n to 0

def generator_func(n):
    while(n>=1):
        yield n
        n-=1
n=int(input("Enter n value:"))
for i in generator_func(n):
    print(i)
print()

#-----------------------------------------------------------------------------------------------------------------------
#all possible unique subsets from a set of distinct integers.

class solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(solution().sub_sets([4, 5, 6]))
print()

#-----------------------------------------------------------------------------------------------------------------------
#iterator that returns numbers, starting with 1, and each sequence will increase by one

class Number:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num<=20:
            x=self.num
            self.num+=1
            return x
        else:
            raise StopIteration

numobj=Number()
numiter=iter(numobj)
for i in numiter:
    print(i)

print()

#-----------------------------------------------------------------------------------------------------------------------
#check whether the said classes are subclasses of the built-in object class or not.

class Student:
	pass
class Marks:
	pass
a=Student()
print(type(a),isinstance(a,Student))
b=Marks()
print(isinstance(b,object))
print()


#-----------------------------------------------------------------------------------------------------------------------
#sort a list of tuples using Lambda


lst=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst.sort(key=lambda y:y[1])
print("After sorting the list are:")
print(lst)
print()


#-----------------------------------------------------------------------------------------------------------------------
#abstract class Box

from abc import ABC
class Box(ABC):
    def add():
        pass
    def empty():
        pass
    def count():
        pass

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
a=item("Nithish",15)
b=item("Akhil",20)
c=item("Kranthi",35)
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
print()


