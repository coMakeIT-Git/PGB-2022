
fruits = ["Apple", "Banana", "Cherry"]
cars = ["Ford", "BMW", "Volvo"]

print("List: ", fruits)
fruits.append("Grapes")
print("Added Grapes: " , fruits)

NewFruits = fruits.copy()
print("Copied List: ", NewFruits)

print("Cherry Count:", fruits.count("Cherry"))

fruits = fruits + cars
print("Merged Lists:" , fruits)

print("Cherry Index:", fruits.index("Cherry"))

fruits.insert(1, "Orange")
print("Inserted Orange at Position 2: ", fruits)

del fruits[1]
print("Deleted element at Position 2: ", fruits)

fruits.remove("Banana")
print("Deleted element Banana: ", fruits)

fruits.reverse()
print("Reverse Order: ", fruits)

cars.sort()
print("Sorted Cars: ", cars)

fruits.clear()
print("Empty List: ", fruits)

