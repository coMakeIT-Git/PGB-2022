"""Create a Time class and initialize it with hours and minutes.
	a. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
	b. Make a method displayTime which should print the time.
	c. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute."""
class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def  addTime(p,q):
        r = Time(0, 0) # creating new object
        r.hours = p.hours + q.hours # sum of hours
        r.minutes = p.minutes + q.minutes # sum of minutes
        while r.minutes >= 60:
            r.hours += 1
            r.minutes -= 60
        return r
    def displayTime(self):
        print("Time is", self.hours,"hours",self.minutes,"minutes")
    def displayMinute(self):
        print("total minutes are",self.hours*60+self.minutes)
a = Time(2, 40)
b = Time(1, 30)
c = Time.addTime(a,b)

c.displayTime()
c.displayMinute()





