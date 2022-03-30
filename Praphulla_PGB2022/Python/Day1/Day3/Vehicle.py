class Vehicle:
    def __init__(self, max_speed, mileage, seating_capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def vehicleType(self, vType, company):
        print("\n Type:\t\t", vType, "\n Company:\t", company)

    def details(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        print("\n **Details**:\n", "Model:\t", model, "\n Color:\t", color, "\n Year of manufacture:\t", year)

    def seating_Capacity(self, capacity):
        self.capacity = capacity
        print("\nThe seating capacity of vehicle is:", capacity)

    def Rent_fare(self):
        return self.capacity * 10

class Taxi(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity
        print("\n Max Speed =\t", max_speed, "\n Mileage =\t", mileage, "\n Maximum Seating Capacity=\t", seating_capacity)
print("\n Class Taxi:")
t = Taxi(90,30,6)
t.vehicleType('Taxi', 'Ford')
t.details('Red', 'Crown Victoria', '1980s')
t.seating_Capacity(4)
print("Total Taxi fare is:", t.Rent_fare())

class Car(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity=5):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def carType(self, cType):
        self.carType = cType
        print("\n Car Type:\t", cType)

    def Rent_fare(self):
            extra = super().Rent_fare()
            extra += extra * 10 / 100 * 1000
            return extra

print("\n Class Car:")
c = Car(130, 20, 4)
c.vehicleType('Car', ' Audi')
c.carType('Cabriolet')
c.details('White', 'A3', '2020s')
c.seating_Capacity(4)
print("Total Car Rent per day is:", c.Rent_fare())


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity=5):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def busType(self, bType):
        self.carType = bType
        print("\n Bus Type:\t", bType)

    def Rent_fare(self):
        extra = super().Rent_fare()
        extra += extra * 10 / 100
        return extra

print("\n Class Bus:")
b = Bus(110, 30, 30)
b.vehicleType('Bus', ' Tata')
b.busType('Private')
b.details('Silver', 'Marcopolo', '2020s')
b.seating_Capacity(20)
print("Total Bus fare is:", b.Rent_fare())











