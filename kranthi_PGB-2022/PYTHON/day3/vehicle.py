# a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage



    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    def fare(self):
        return self.capacity*100


#Bus class inheriting the Vehicle class
class bus(Vehicle):
    def __init__(self,name, max_speed, mileage,capacity=5):
        self.capacity=capacity
        Vehicle.__init__(self, name, max_speed, mileage)

    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"
    def fare(self):
        return self.capacity*100+((self.capacity*100)*0.01)

obj1=bus("school bus", 120, 16,40)
print(obj1.seating_capacity())
print("Fare collected by the bus is:")
print(obj1.fare())
#Taxi class is inheriting the Vehicle class
class taxi(Vehicle):
    def display(self):
        print("taxi name is:",self.name)
        print("taxi maximaum speed is",self.max_speed)
        print("taxi mileage is",self.mileage)
obj=taxi("skycabs",100,18)
print(obj.display())



