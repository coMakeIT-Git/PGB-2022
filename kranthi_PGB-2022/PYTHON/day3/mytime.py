#Create a Time class and initialize it with hours and minutes.

class mytime:
    def __init__(self,hrs,mins):
        self.hrs=hrs
        self.mins=mins

#Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
    def addTime(t1,t2):
        t3=mytime(0,0)
        t3.hrs=t1.hrs+t2.hrs
        t3.mins=t1.mins+t2.mins
        while t3.mins>=60:
            t3.hrs+=1
            t3.mins=t1.mins+t2.mins-60
        return t3
# Make a method displayTime which should print the time.
    def display(self):
        print("The time is {} hours and {} mins".format(self.hrs,self.mins))
#Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
    def displayMins(self):
        print("total minutes are {}".format(self.hrs*60+self.mins))
a=mytime(2,50)
b=mytime(1,20)
c=mytime.addTime(a,b)
print("Sum of times:")
print(c.hrs,c.mins)
c.display()
c.displayMins()