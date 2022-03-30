
#Create a Time class and initialize it with hours and minutes.
# a.Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)


class Time():
    #initialise
    def __init__(self,hours,mins):
        self.hours=hours
        self.mins=mins
        
    def add(t1,t2):
        t3=Time(0,0)
        if(t1.mins+t2.mins > 60):
            t3.hours=(t1.mins+t2.mins)/60
        
        t3.hours=t3.hours+t1.hours+t2.hours
        t3.mins = (t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
        return t3
    
    #b.Make a method displayTime which should print the time.
    def displaytime(self):
        print("Time is {} hours and {}".format(self.hours,self.mins))
        
    #c.Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
    
    def displayMinute(self):
        print("Time in minutes {}".format((self.hours*60)+self.mins))
        

x=Time(2,50)
y=Time(1,20)
z=Time.add(x,y)
z.displaytime()
z.displayMinute()
        