fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.append("Berry")  # Added element
print(fruits)
copyF = fruits.copy()  # Copied list to another
print(copyF)
fruits.insert(4, "cherry")  # inserted element at specific location
count: int = fruits.count('cherry')  # counted the element occurrence
print(count)
fruits.extend(cars)  # extended the existing list with elements of other
print(fruits)
x = fruits.index('BMW')  # returned index of specific element
print(x)
fruits.pop(2)  # removed 2nd element
print(fruits)
fruits.remove('banana')  # removed banana
print(fruits)
st = fruits[::-1]  # reversed the list
print(st)
cars.sort()  # sorted the car list
print(cars)
fruits.clear()  # Used clear to delete elements in fruits list
