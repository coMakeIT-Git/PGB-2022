s = set()
s.add(1)
s.add(2)
s.add(3)
print("Set: ", s)
s.remove(3)
print("Removed 3:", s)


#Set Operations
x = set([1,2,3,4,5,6,7,8,9,0,21,34,56,99])
y = set([1,9,2,21,34,56,99])
print()
print("Set X: ", x)
print("Set Y: ", y)
print("\nX-Y: ", x.difference(y))

print("\nRemoving common items:")
intersect = x.intersection(y)
x = x - intersect
y = y - intersect
print("Set X: ", x)
print("Set Y: ", y)

x = set([1,2,3,4,5,6,7,8,9,0,21,34,56,99])
y = set([1,9,2,21,34,56,99])

print("\nX and Y are Disjoint: ", x.isdisjoint(y))
print("\nX is a subset of Y: ", x.issubset(y))
print("\nY is a subset of X: ", x.issuperset(y))
print("\nUnion: ", x.union(y))
print("\nUnion using |: ", x|y)
print("\nSymmetric Difference: ", x.symmetric_difference(y))



