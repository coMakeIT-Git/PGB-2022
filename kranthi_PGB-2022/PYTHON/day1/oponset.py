myset=set("kranthi")
print(myset)
myset.add('y')
print("Adding a element to set using myset.add():")
print(myset)
myset.remove('t')
print("Removing letter 't' element from the set")
print(myset)
setx=set()
sety= set()

for i in range(1,5):
    setx.add(i)
for i in range(3,9):
    sety.add(i)
print(setx)
print(sety)
print(" elements in setx but not in sety")
set2=setx-sety
print(set2)
print("set of elements common in both sets")
setz=setx.intersection(sety)
print(setz)
print("Return True if no items in set x is present in set y")
if (setx &sety):
    print(False)
else:
    print(True)
print("Return True if all items in set x are present in set y")
if(setx<sety):
    Print(True)
else:
    print(False)
print("Return True if all items in set y are present in set x")
if(sety<setx):
    Print(True)
else:
    print(False)
print("Return a set that contains all items from both sets, except items that are present in both sets:")
set5=(setx|sety)-setz
print(set5)
print("Remove the items that are present in both sets, AND insert the items that is not present in both sets")
set6=setx|set5
print(set6)
print("Return a set that contains all items from both sets, duplicates are excluded")
set7=setx|sety
print(set7)
print("Insert the items from set y into set x")
setx.update(sety)
print(setx)

