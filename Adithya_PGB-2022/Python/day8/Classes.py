class vehicle:
	capacity=0
	wheels=4
	def __init__(this,max_speed,milage):
		this.max_speed=max_speed
		this.milage=milage
class Car(vehicle):
	def __init__(this,max_speed,milage):
		this.max_speed=max_speed
		this.milage=milage
	def print(this):
		print(this.max_speed,this.milage)
class Bus(vehicle):
	def __init__(this,max_speed,milage):
		this.max_speed=max_speed
		this.milage=milage
	def print(this):
		print(this.max_speed,this.milage)
	def seating_capacity(this,capacity=5):
		this.capacity=capacity
	def final_fare(this):
		fare=100*this.capacity
		final=fare+fare*0.1
		return final
Taxi=Car(50,20)
print(Taxi.print())
n=Bus(50,20)
n.seating_capacity(50)
print(n.final_fare())



class Time:
	def __init__(this,hours,minutes):
		this.hours=hours
		this.minutes=minutes
	def addTime(this,first,second):
		this.minutes=first.minutes+second.minutes
		this.hours=0
		if(this.minutes>60):
			this.hours=1
			this.minutes=this.minutes-60
		this.hours+=first.hours+second.hours
		return this.hours,this.minutes
	def displayTime(this):
		print(this.hours,this.minutes)
	def DisplayMinute(this):
		minutes=this.hours*60
		minutes+=this.minutes
		print(minutes)
print(Time(1,2).addTime(Time(2,50),Time(1,20)))
Time(2,40).DisplayMinute()
