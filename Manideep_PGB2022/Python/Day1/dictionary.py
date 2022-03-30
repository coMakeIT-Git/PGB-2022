# Create a dictionary  and and apply respective inbuilt method to
# 	a. Return the value of the specified key
# 	b. Print all key, value pairs
# 	c. Remove the element with the specified key
# 	d. Remove the last inserted key-value pair

x = ('key1', 'key2', 'key3')
y = '5'

d = dict.fromkeys(x, y)
print(d)


d={'a':0,'b':1,'c':2}
print('enter key')
k=input()
print(d.get(k))

print(d.keys())
print(d.values())
print('enter key to delete')
k=input()
del d[k]
print(d)

lastinsertkey=list(d.keys())[-1]
print(lastinsertkey)
del d[lastinsertkey]
print(d)