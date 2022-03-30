print("***Tuples***")
tup = 1, 2, 4, 6, 21, 43, 1, 4, 2, 6, 6
print("Tuple: ", tup)
print("Count of 6: ", tup.count(6))
print("Index of 6: ", tup.index(6))

print()
print("***Dictionaries***")
tup1 = "one", "two", "three"
tup2 = 5
d = dict.fromkeys(tup1, tup2)
print("Dictionary:", d)
print("All Pairs: ", d.items())
print("Value of key One: ", d.get("one"))
d.pop("one")
print("Removed element at key One: ", d)
print("Last inserted value removed: ", d.popitem())
print("Dictionary:", d)

