class Vehicle:
    def __init__(self, name, max_mileage, capacity,max_speed):
        self.name = name
        self.max_mileage = max_mileage
        self.capacity = capacity
        self.max_speed = max_speed
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    def fare(self):
        return self.capacity * 100
class car(Vehicle):
    pass
class Taxi(Vehicle):
    pass

taxi=Taxi("taxi",180,90,20)
print("Taxi's  name {} and maxspeed {} and mileage {}".format(taxi.name,taxi.max_speed,taxi.max_mileage))

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

bus= Bus("School Volvo", 180, 250 ,2550)
print("Total Bus fare is:", bus.fare())
print(bus.seating_capacity())
