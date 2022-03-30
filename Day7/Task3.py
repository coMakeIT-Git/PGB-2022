#Create an inner function to calculate the addition in the following way
	#a. Create an outer function that will accept two parameters, a and b
	#b. Create an inner function inside an outer function that will calculate the addition of a and b
	#c. At last, an outer function will add 5 into addition and return it
def outer(a,b):
    def add(a,b):
        c=a+b
        return c
    res=add(a,b)
    return res
print("output:",outer(2,3))