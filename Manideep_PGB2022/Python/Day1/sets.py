
s=set()
s.add(1)
s.add(2)
s.add(1)
print(s)
s.remove(1)
print(s)


x=set([1,2,3,5,7,12])
y=set([1,2,5,7,10])
print(x.difference(y)) 
x.difference_update(y)   #Remove the items that exist in both sets
print(x.isdisjoint(y))  # Return True if no items in set x is present in set y
print(x.issubset(y))    # Return True if all items set x are present in set y
print(y.issubset(x))    # Return True if all items set y are present in set x
print(x.symmetric_difference(y)) #return a set that contains all items from both sets, except items that are present in both sets
x.symmetric_difference_update(y)  # Remove the items that are present in both sets, AND insert the items that is not present in both sets
print(x)
print((x.union(y)))    # Return a set that contains all items from both sets, duplicates are excluded
x.update(y)            # Insert the items from set y into set x
print(x)