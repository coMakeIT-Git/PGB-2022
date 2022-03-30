#class Vehicle
class Vehicle:
	no_ofWheels = 4
	def __init__(this,maxspeed,mileage,capacity):
		this.maxspeed = maxspeed
		this.mileage = mileage
		this.capacity = capacity
	
	def getspecs(this):
		print("MaxSpeed:",this.maxspeed," Mileage:",this.mileage," Capacity:",this.capacity," no_ofWheels:",Vehicle.no_ofWheels)
	
	def seating_capacity(this):
		print("Vehicle Capacity:",this.capacity)
	
	def fare(this):
		return this.capacity*100
	
	
#class Taxi	
class Taxi(Vehicle):
	pass


#class car
class Car(Vehicle):
	def __init__(this,maxspeed,mileage,capacity=5):
		super().__init__(maxspeed,mileage,capacity)


#class bus
class Bus(Vehicle):
	def fare(this):
		charge = (10/100)*(super().fare())
		return (this.capacity*100)+charge	
		
		
#class time
class Time:
	def __init__(this,hours,mins):
		this.hrs = hours
		this.mins = mins
		
	def displayTime(this):
		print("Time is",this.hrs," hours and ",this.mins," minutes")
			
	def addTime(this,t):
		hurs = this.hrs+t.hrs
		mins = this.mins+t.mins
		if(mins >= 60):
			hurs += 1
			mins -= 60
		print("Time is",hurs," hours and ",mins," minutes")	
		
	def DisplayMinutes(this):
		print("Time in minutes:",(this.hrs)*60+this.mins)
		

t = Taxi(234,13,4)
print("Taxi:")
t.getspecs()
print("Taxi fare:",t.fare())

c = Car(200,20)
print("car:")
c.getspecs()
c.seating_capacity()

bus = Bus(126,18,30)
print("Bus:")
bus.getspecs()
bus.seating_capacity()
print("BusFare:",bus.fare())


t1 = Time(2,56)
t1.displayTime()
t1.DisplayMinutes()
t2 = Time(1,45)
t2.displayTime()
t2.DisplayMinutes()
t1.addTime(t2)


















	
