import random
r = 21
print(r)
q = "Shyam sai Dogga"  # str
print(q)
p = 16.75  # float
print(p)
o = complex(2, 3)  # complex
print(o)
n = ["Mouse", "Keyboard", "Console"]  # list
print(n)
l = ("Mouse", "Keyboard", "Console")  # tuple
print(l)
k = random.randrange(90, 100)  # range
print(k)
j = {"name": "Shyam sai Dogga", "CMIT.No": "CMI-T1097"}  # dict
print(j)
i = {"Mouse", "Keyboard", "Console"}  # set
print(i)
h = frozenset({"Mouse", "Keyboard", "Console"})  # frozenset
print(h)
g = True  # bool
print(g)
f = b"Shyam"  # bytes
print(f)
e = bytearray(8)  # bytearray
print(e)
print("Lists are mutable:")
n[0] = "PenDrive"
print(n)
print("Sets are mutable:")
i.add('2')
print(i)
print("Dictionaries are mutable:")
j["name"] = "coMakeIT"
print(j)
print('The rest all are immutable (ie.., Tuples,Sets etc: )')
l[1] = "PenDrive"
print(l)
