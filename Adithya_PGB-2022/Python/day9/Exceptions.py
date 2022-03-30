
try:
	x=1
	y=0
	z = x/y
except ZeroDivisionError:
    z = 0
try:
	import math.n
except ImportError:
	print("Wrong Import")
try:
	a=[1,2]
	a[3]=1
except IndexError:
	print("Wrong Index")
try:
	import error
except IndentationError:
	print("Wrong Indentation")
try:
	a=int('a')
except ValueError:
	print(ValueError)
try:
	a=ze+a
except Exception:
	print("Some exception")
a=5
b=int(input("give integer input"))
try:
	c=a+b
except Exception as e:
	print(e)
else:
	print(c)
finally:
	b=5
	print(a+b)
