#TASK6

fruits=['apple', 'banana', 'cherry']#CREATED A LIST fruit
cars = ['Ford', 'BMW', 'Volvo']#CREATED A LIST cars

#Add an element to the fruits list
fruits.append("mango")
print(fruits)

#Remove all elements from the fruits list
fruits.clear()
print(fruits)

# Copy the fruits list
fruits2=['apple', 'banana', 'cherry']
new_fruits=fruits2.copy()
print(new_fruits)

#Return the number of times the value "cherry" appears in the fruits list
fruit3=['apple','cherry','banana','cherry']
occur=fruit3.count("cherry")
print(occur)

#Add the elements of cars to the fruits list
fruits4=['apple', 'banana', 'cherry']
cars1= ['Ford', 'BMW', 'Volvo']
fruits4.extend(cars1)
print(fruits4)

#What is the position of the value "cherry"
index = fruits4.index('cherry')
print(index)

#Insert the value "orange" as the second element of the fruit list
fruits5=['apple','banana','cherry']
fruits5.insert(2,'orange')
print(fruits5)

#Remove the second element of the fruit list
fruits6=['apple','banana','cherry']
fruits6.pop(2)
print(fruits6)

#Remove the "banana" element of the fruit list
fruits7=['apple','banana','cherry']
fruits7.remove('banana')
print(fruits7)

#Reverse the order of the fruit list
fruits7=['apple','banana','cherry']
fruits7.reverse()
print(fruits7)

#Sort the cars list
cars1= ['Ford', 'BMW', 'Volvo']
cars1.sort()
print(cars1)