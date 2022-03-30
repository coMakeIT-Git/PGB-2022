class Vehicle:
    #Class attribute
    City = "London"
    def __init__(self, max_speed, mileage, seating_capacity):
        #Instance attributes
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity
    #default method
    def fare(self):
        return self.seating_capacity * 100

class Taxi(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

class Car(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity=5):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity
    #Overridden method for Bus
    def fare(self):
        maintenance = 0.1 * self.seating_capacity * 100
        return self.seating_capacity * 100 + maintenance

print("City: ", Vehicle.City)

print("\n***Taxi***")
taxi = Taxi(100, 20, 4)
print("Max Speed:", taxi.max_speed, "\nMileage:", taxi.mileage, "\nSeating Capacity:", taxi.seating_capacity)
print("Fare:", taxi.fare())

print("\n***Car***")
car = Car(140, 30)
print("Max Speed:", car.max_speed, "\nMileage:", car.mileage, "\nSeating Capacity:", car.seating_capacity)
print("Fare:", car.fare())

print("\n***Bus***")
bus = Bus(120, 10, 30)
print("Max Speed:", bus.max_speed, "\nMileage:", bus.mileage, "\nSeating Capacity:", bus.seating_capacity)
print("Fare:", bus.fare())