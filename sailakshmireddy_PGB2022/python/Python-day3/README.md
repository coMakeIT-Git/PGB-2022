1. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
	a. Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it.
	b. Create a Car class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 5
	c. Define a property that must have the same value for every class instance (object).
	d. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
6. Create a Time class and initialize it with hours and minutes.
	a. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
	b. Make a method displayTime which should print the time.
	c. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
7. Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations
8. Write a Python class to get all possible unique subsets from a set of distinct integers. 
	Input : [4, 5, 6]
	Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
9. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
	Note: Do not use the same element twice.
	Input: numbers= [10,20,10,40,50,60,70], target=50
	Output: 3, 4
10. Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
	Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
	Output : [[-10, 2, 8], [-7, -3, 10]]
11. Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.
12. Write a Python program to sort a list of tuples using Lambda.
	Original list of tuples:
	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
	Sorting the List of Tuples:
	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
13. Write a Python program to sort a list of dictionaries by color using Lambda.
	Original list of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
	Sorting the List of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
14. Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
	Original dictionary of lists:
	{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
	Split said dictionary of lists into list of dictionaries:	
	[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language':80}]
15. Write a Python program to convert a given list of tuples to a list of strings using map function.
	Original list of tuples:
	[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
	
	Convert the said list of tuples to a list of strings:
	['red pink', 'white black', 'orange green']
16. Write a generator function which takes an integer n as a parameter. The function should return a generator which counts down from n to 0. Test your function using a for loop.
17. Write an “abstract” class, Box, and use it to define some methods which any box object should have: 
	a. add, for adding any number of items to the box, 
	b. empty, for taking all the items out of the box and returning them as a list, and 
	c. count, for counting the items which are currently in the box. 
	d. Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects. 
	e. Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.
18. Commit code to the GIT