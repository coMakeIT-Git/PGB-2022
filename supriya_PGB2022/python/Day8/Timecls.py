#Create a Time class and initialize it with hours and minutes.
#a. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
#b. Make a method displayTime which should print the time.
#c. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
class Timecls():

	def __init__(self, hrs, mins):
		self.hrs = hrs
		self.mins = mins

	def addTime(t1, t2):
		t3 = Timecls(0,0)
		if t1.mins+t2.mins > 60:
			t3.hrs = (t1.mins+t2.mins)/60
		t3.hrs = t3.hrs+t1.hrs+t2.hrs
		t3.mins = (t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
		return t3

	def displayTime(self):
		print ("Time in hours:",self.hrs,"hours")

	def displayMinute(self):
		print ("Time in minutes:",(self.hrs*60)+self.mins)

a = Timecls(2,50)
b = Timecls(1,20)
c = Timecls.addTime(a,b)
c.displayTime()
c.displayMinute()