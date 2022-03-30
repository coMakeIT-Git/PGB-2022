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

    def displayTime(self):
        print("\n **Time:**", "\n Hours:\t", self.hours, "\n Minutes:\t", self.minutes)

    def displayMinutes(self):
        print("\n Displaying Minutes:\t", (self.hours * 60) + self.minutes)

f = Time(9, 30)
e = Time(6, 40)
d = Time.addTime(f, e)
d.displayTime()
d.displayMinutes()

h1, m1=map(int, input("\n Enter time in 00hrs:00min Format:").split())
h2, m2=map(int, input("\n Enter time in 00hrs:00min Format:").split())
f = Time(h1, m1)
e = Time(h2, m2)
d = Time.addTime(f, e)
d.displayTime()
d.displayMinutes()