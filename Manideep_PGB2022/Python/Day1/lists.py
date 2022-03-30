from traceback import print_tb


fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo'] 

fruits.append('grapes')  # added to fruits
fruits.append('cherry') 
print(fruits) 
fruits_copy=fruits[:]    # copy of fruits
fruits.clear()           # removing all elements  from fruits
print(fruits,fruits_copy)
print(fruits_copy.count('cherry')) # count of cherry in fruits
fruits_copy.extend(cars)  #adding cars to fruits
print(fruits_copy)
print(fruits_copy.index('cherry'))  # index of cherry
fruits_copy.insert(1,'orange')      # Insert the value "orange" as the second element of the fruit list
print(fruits_copy)
fruits_copy.pop(1)                  # Remove the second element of the fruit list
print(fruits_copy)
fruits_copy.remove('banana')        # Remove the "banana" element of the fruit list
print(fruits_copy)
fruits_copy.reverse() # Reverse the order of the fruit list
print(fruits_copy)
fruits_copy.sort() # Sort the cars list 
print(fruits_copy)
