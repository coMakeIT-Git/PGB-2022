class MyNumbers:
	def __iter__(this):
		this.a=1
		return this
	def __next__(this):
		x=this.a
		this.a+=1
		return x
myclass = MyNumbers()
myiter = iter(myclass)

for i in range(1,21):
	print(next(myiter))
