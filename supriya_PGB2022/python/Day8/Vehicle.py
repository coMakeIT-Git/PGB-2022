#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
#a. Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it.
#b. Create a Car class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 5
#c. Define a property that must have the same value for every class instance (object).
#d. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. 
#If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
class Vehicle:
    def __init__(self, max_speed, price):
        self.max_speed = max_speed
        self.price = price
    def seating_capacity(self,capacity):
        return f"The seating capacity for car is {capacity}"
v=Vehicle(120,4000000) #object
print("Vehicle with maxspeed {} and price {}".format(v.max_speed,v.price))
class Cab(Vehicle):
    pass
cab=Cab(12,300)
print("Cab's maxspeed {} and price {}".format(cab.max_speed,cab.price))
class Audi(Vehicle):
    def seating_capacity(self, capacity=4):
        return super().seating_capacity(capacity=4)
audi=Audi(208,3400000)
print(audi.seating_capacity())
class Dirtbike(Vehicle):
    pass
dirtbike=Dirtbike(180,200000)
print("Dirtbike maxspeed is {} and price is {}".format(dirtbike.max_speed,dirtbike.price))
print("Audi's max speed is {} and price is {}".format(audi.max_speed,audi.price))
