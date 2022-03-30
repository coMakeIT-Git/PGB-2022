class Vehicle:
    wheels = "Four"

    def __init__(self, max_speed, mileage, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def model(self, version):
        return f"The version of a vehicle with mileage {self.mileage} is under {version}"

    def seating_capacity(self, changecapacity):
        return f"The seating capacity of this {self.max_speed}km/h car is {changecapacity} passengers"

    def fare(self):
        return self.capacity * 100


class Car(Vehicle):
    def model(self, version="HighEnd"):
        return super().model(version="HighEnd")


class Bus(Vehicle):
    def fare(self):
        extra = super().fare()
        extra += extra * 10 / 100
        return extra


bus = Bus(150, 15, 50)
print("Total Bus fare is:", bus.fare())

Taxi = Car(190, 22, 4)
print(Taxi.seating_capacity(5))
print(Taxi.model())
print(Car.wheels)
print(Taxi.wheels)
