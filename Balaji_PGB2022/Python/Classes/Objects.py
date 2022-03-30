class Vehicle:
    colour="Black"
    def __init__(self,max_speed,mileage,capacity):
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity
    def display(self):
        print("Maximum speed is:",self.max_speed)
        print("Maximum mileage is:",self.mileage)
        print("Maximum capacity of bus is:",self.capacity)

    def Seating_Capacity(self, capacity):
       print("Seating Capacity of Vehicle is:", capacity)

    def fair_charge(self):
        return self.capacity*100

class Taxi(Vehicle):
    taxiobj=Vehicle(160,20,10)
    taxiobj.display()

class Car(Vehicle):
    pass
class Bus(Vehicle):
    def __init__(self,max_speed,mileage,capacity=5):
        return super().__init__(max_speed,mileage,capacity)
    def fair_charge(self):
        charge=super().fair_charge()
        percent=(10/100)*charge
        charge+=percent
        return charge
carobj=Car(160,20,10)
busobj=Bus(160,20,30)
busobj.Seating_Capacity(30)
print("Fair charge of bus is:",busobj.fair_charge())

#check whether the said classes are subclasses of the built-in object class or not.
class student:
	pass
class Marks:
	pass
a=student()
print(type(a),isinstance(a,student))
b=Marks()
print(isinstance(b,object))




