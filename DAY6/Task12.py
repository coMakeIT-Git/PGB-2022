#TASK12


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#Return a set that contains the items that only exist in set x, and not in set y
print(A-B)

#Remove the items that exist in both sets
print(A^B)

#Return True if no items in set x is present in set y
x={1,2,3}
y={4,5,6}
print(x.isdisjoint(y))

#Return True if all items in set x are present in set y
x={1,2,3}
y={1,2,3,4,5}
z = y.issuperset(x)
print(z) 

#Return True if all items set y are present in set x
p = x.issuperset(y)
print(p) 

# Return a set that contains all items from both sets, except items that are present in both sets
res = A^B
print(res)



#Remove the items that are present in both sets, AND insert the items that is not present in both sets
res=A^B
z = A.intersection(B)
res.update(z)
print(res)

#Insert the items from set y into set x
x={2,6}
y={1,3}
x.update(y)
print(x)
