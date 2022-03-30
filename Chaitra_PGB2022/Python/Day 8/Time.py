import time
import datetime
from datetime import datetime, timedelta

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.time = str(hours) + ":" + str(minutes)
        self.obj = datetime.strptime(self.time, '%H:%M')

    def addTime(self, time1, time2):
        change = timedelta(hours=t2.hours, minutes=t2.minutes)
        t1.obj += change
        print(t1.obj.hour, t1.obj.minute, sep=":")

    def displayTime(self):
        print(self.obj.hour, self.obj.minute, sep=":")

    def displayMinute(self):
        m = self.hours * 60 + self.minutes
        print(m)

print("Enter time in HH:MM format")
h1, m1 = map(int, input("Time 1 - ").split(":"))
h2, m2 = map(int, input("Time 2 - ").split(":"))

t1 = Time(h1, m1)
t2 = Time(h2, m2)

#Diplaying Time
print("\nDisplaying Times...")
t1.displayTime()
t2.displayTime()

#Displaying time in minutes
print("\nDisplaying Times in minutes...")
t1.displayMinute()
t2.displayMinute()

#Adding the two times
print("\nAdding Times...")
t1.addTime(t1, t2)

