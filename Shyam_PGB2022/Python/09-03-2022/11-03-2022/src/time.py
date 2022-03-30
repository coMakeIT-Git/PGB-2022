class Time():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(a, b):
        c = Time(0, 0)
        if a.minutes + b.minutes > 60:
            c.hours = (a.minutes + b.minutes) // 60
        c.hours = c.hours + a.hours + b.hours
        c.minutes = (a.minutes + b.minutes) % 60
        return c

    def displaytime(self):
        print("Time - ", self.hours, ":", self.minutes, "minutes.")

    def displayminute(self):
        print((self.hours * 60) + self.minutes)


f = Time(9, 30)
e = Time(6, 40)
d = Time.addTime(f, e)
d.displaytime()
d.displayminute()
