#TASK4

#assign to multiple values and can be of different data types
x, y, z = 0.1, 100, 'string'
print(x)# 0.1
print(y)# 100
print(z)# string

#same object is assigned to all variables, so if you change the value of element or add a new element, the other will also change.
a = b = [0, 1, 2]
print(a is b)# True
a[0] = 100
print(a)# [100, 1, 2]
print(b)# [100, 1, 2]