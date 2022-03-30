# 1. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
# 	a. Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it.
# 	b. Create a Car class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 5
# 	c. Define a property that must have the same value for every class instance (object).
# 	d. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle:
    color = "Red"

    def __init__(self, max_speed, mileage, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        f = self.capacity * 100
        return f

    def display(self):
        return f"{self.__class__.__name__} Max Speed : {self.max_speed} Mileage : {self.mileage}, Capacity : {self.capacity}"


Taxi = Vehicle(40, 50, 4)
print(Taxi.display())
print(f"Total Fare : {Taxi.fare()}")


class Car(Vehicle):
    pass


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity=5):
        super().__init__(max_speed, mileage, capacity)

    def fare(self):
        cost = super().fare()
        cost += cost * 0.1
        return cost


College_Bus = Bus(40, 30, 20)
print(College_Bus.display())
print(f"Total Fare : {College_Bus.fare()}")

print("\n\n")

# 6. Create a Time class and initialize it with hours and minutes.
# 	a. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 	b. Make a method displayTime which should print the time.
# 	c. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, time_a, time_b):
        minutes = time_a.minutes + time_b.minutes
        hours = time_a.hours + time_b.hours
        if minutes >= 60:
            minutes = minutes - 60
            hours += 1
        self.minutes = minutes
        self.hours = hours
        return f"{hours} hour and {minutes} mins"

    def displayTime(self):
        print(f"{self.hours} hour and {self.minutes} mins")

    def DisplayMinute(self):
        minutes = (self.hours * 60) + self.minutes
        print(f"{minutes} minutes")
        return minutes


t1 = Time(2, 50)
t1.displayTime()
t2 = Time(1, 20)
t2.displayTime()

t3 = t2
print(t3.addTime(t1, t2))
t3.DisplayMinute()