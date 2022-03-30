 #Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
	#a. Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it.
	#b. Create a Car class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 5
	#c. Define a property that must have the same value for every class instance (object).
	#d. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare."""
class Vehicle:#vehicle class
    def __init__(self, name, max_mileage, capacity,max_speed):
        self.name = name
        self.max_mileage = max_mileage
        self.capacity = capacity
        self.max_speed = max_speed
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    def fare(self):
        return self.capacity * 100
class car(Vehicle):#car class
    pass
class Taxi(Vehicle):# taxi class
    pass

taxi=Taxi("taxi",180,90,20)
print("Taxi's  name {} and maxspeed {} and mileage {}".format(taxi.name,taxi.max_speed,taxi.max_mileage))

class Bus(Vehicle):#bus class
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

bus= Bus("School Volvo", 180, 250 ,2550)
print("Total Bus fare is:", bus.fare())
print(bus.seating_capacity())