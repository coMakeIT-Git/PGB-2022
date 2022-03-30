class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def add_time(time1,time2):
        time3=Time(0,0)
        time3.hours=time1.hours+time2.hours
        time3.minutes=time1.minutes+time2.minutes
        while(time3.minutes>=60):
            time3.hours+=1
            time3.minutes=time3.minutes-60
        return time3
    def display_time(self):
        print("The Time is",self.hours,"hours and",self.minutes,"minutes")
    def display_minute(self):
        minute=0
        if(self.hours>=1):
            minute+=60
            self.hours-=1
        minute+=self.minutes
        print("Total minutes in the time are:",minute)

obj1=Time(1,59)
obj2=Time(1,59)
timeobj=Time.add_time(obj1,obj2)
timeobj.display_time()
timeobj.display_minute()

