# Write a class to handle below exceptions
# 	a. ZeroDivisionError
# 	b. ImportError
# 	c. IndexError
# 	d. IndentationError
# 	e. ValueError
# 	f. Exception
# 	g. Raise any exception and handle it properly and use else, finally blocks to print something irrespective of exception

from collections import *
a=[1,2,3]
try:
    print(a)
    #print(combinations(a))
    for i in range(2):
        print("Helio")
    print(a[3])
    print(1/0)
    a='ab'
    k=int(a)
except ZeroDivisionError as e:
    print(e)
except ImportError as e:
    print(e)
except IndexError as e:
    print(e)
except ImportError as e:
    print(e)
except ValueError as e:
    print(e)

finally:
    print('this will execute always ')