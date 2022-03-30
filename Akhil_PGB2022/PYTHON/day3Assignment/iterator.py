class myiter:
	def __iter__(this):
		this.x = 1
		return this
	def __next__(this):
		if this.x<=50:
			a = this.x
			this.x += 1
			return a
		else:
			raise StopIteration

c = myiter()
myiter = iter(c)

for i in myiter:
	print(i)
