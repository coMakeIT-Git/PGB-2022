a = {"Shyam sai Dogga", 21, "CMI-T1079"}
a.add("Acc.2022")
print(a)
b = {"Cricket", "FootBall", "Sport"}
a.update(b)
print(a)
a.discard("Sport")
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6}
print(a.difference(b))  # elements not in b but in a
print(b.difference(a))  # elements not in a but in b
print(a.intersection(b))  # common elements
print(a.isdisjoint(b))  # return boolean if a= or !=b
z = a.symmetric_difference(b)  # removes common elements in both
print(z)
print(a.issuperset(b))  # returns boolean if it is superset
print(b.issubset(a))  # returns boolean if it is subset
print(a.union(b))  # all items from both sets
a.update(b)  # it appends b elements to a and stores
print(a)
a.symmetric_difference_update(b)  # removes all and insert the common and updates
print(a)
