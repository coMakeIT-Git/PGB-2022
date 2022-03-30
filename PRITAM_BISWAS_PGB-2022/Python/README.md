
### DAY 1

1. Setup any IDE to execute python code ex: Pycharm
2. Define variables for each data type and store respective data
3. Try to modify the data and identify which data types are mutable and which are immutable
4. Create variables and assign multiple values and override the data types
5. Define variable 'a' and store int and string types using + operator and resolve errors if any
	define variable 'b' and sore string and boolean types using + operator and resolve errors if any
	define variable 'c' and sote list and tuple types using + operator and resolve errors if any
6. create a list fruits = ['apple', 'banana', 'cherry'], cars = ['Ford', 'BMW', 'Volvo'] and apply respective inbuilt method to
	a. Add an element to the fruits list
	b. Remove all elements from the fruits list
	c. Copy the fruits list
	d. Return the number of times the value "cherry" appears in the fruits list
	e. Add the elements of cars to the fruits list
	f. What is the position of the value "cherry"
	g. Insert the value "orange" as the second element of the fruit list
	h. Remove the second element of the fruit list
	i. Remove the "banana" element of the fruit list
	j. Reverse the order of the fruit list
	k. Sort the cars list 
7. Create a string
	a. Convert it into upper case
	b. Convert into lower case
	c. Return the number of times a specified value occurs in a string
	d. Return true if the string ends with the specified value
	e. Return True if all characters in the string are in the alphabet
	f. Convert the first character of each word to upper case
	g. Convert the first character to upper case
	h. Search the string for a specified value and returns the position of where it was found
	i. Reverse the string with slicing
8. Create a tuple and
	a. Return the number of times a specified value occurs in a tuple
	b. Search the tuple for a specified value and returns the position of where it was found
9.  Create a dictionary with 3 different keys, all with the value '5' using inbuilt method
10. Create a dictionary  and and apply respective inbuilt method to
	a. Return the value of the specified key
	b. Print all key, value pairs
	c. Remove the element with the specified key
	d. Remove the last inserted key-value pair
11. Create a Set and apply inbuild methods to 
	a. Add an element to the set
	b. Remove specific element
12. create 2 sets x and y and 
	a. Return a set that contains the items that only exist in set x, and not in set y
	b. Remove the items that exist in both sets
	c. Return True if no items in set x is present in set y
	d. Return True if all items in set x are present in set y
	e. Return True if all items set y are present in set x
	f. Return a set that contains all items from both sets, except items that are present in both sets
	g. Remove the items that are present in both sets, AND insert the items that is not present in both sets
	

### DAY 2



1. Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
2. Write a program to create a function show_employee() using the following conditions.
	a. It should accept the employee’s name and salary and display both.
	b. If the salary is missing in the function call then assign default value 9000 to salary
3. Create an inner function to calculate the addition in the following way
	a. Create an outer function that will accept two parameters, a and b
	b. Create an inner function inside an outer function that will calculate the addition of a and b
	c. At last, an outer function will add 5 into addition and return it
4. Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
5. Assign a different name to function and call it through the new name
	Ex: Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
6. Find the largest item from a given list without using inbuilt methods
7. Convert string into a datetime object
	Input : date_string = "Mar 09 2022 11:20AM"
	output: 2022-03-09 11:20:00
8. Calculate the date 4 months from the current date 
9. Generate 6 digit random secure OTP
10. Generate a random Password which meets the following conditions
	a. Password length must be 10 characters long.
	b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
11. Write a program to use for loop to print the following reverse number pattern

		5 4 3 2 1 
		4 3 2 1 
		3 2 1 
		2 1 
		1
12. Count all letters, digits, and special symbols from a given string
13. Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
14. Write a program to remove special symbols / punctuation from a string
	Ex : str1 = "/*We are le@arning python@67 fun_da**mentals**"
	Output: We are learning python fundamentals
15. Write a program to removal all characters from a string except integers
	Input : str1 = 'I am 20 years and and 22 months old'
	Output : 2022
16. Write a program to find words with both alphabets and numbers from an input string.
	Input : str1 = "Sriman25 is Data scientist50 and AI Expert"
	Output : ['Sriman25','Scientist50']
17. Commit the code to Git 


### DAY 3

1. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
    a. Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it.
    b. Create a Car class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 5
    c. Define a property that must have the same value for every class instance (object).
    d. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
2. Create a Time class and initialize it with hours and minutes.
    a. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
    b. Make a method displayTime which should print the time.
    c. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
3. Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations
4. Write a Python class to get all possible unique subsets from a set of distinct integers. 
    Input : [4, 5, 6]
    Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
    Note: Do not use the same element twice.
    Input: numbers= [10,20,10,40,50,60,70], target=50
    Output: 3, 4
6. Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
   Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
   Output : [[-10, 2, 8], [-7, -3, 10]]
7. Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.
8. Write a Python program to sort a list of tuples using Lambda.
   Original list of tuples:
   [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
   Sorting the List of Tuples:
   [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
9. Write a Python program to sort a list of dictionaries by color using Lambda.
   Original list of dictionaries :
   [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
   Sorting the List of dictionaries :
   [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
10. Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
    Original dictionary of lists:
    {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
    Split said dictionary of lists into list of dictionaries:	
    [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language':80}]
11. Write a Python program to convert a given list of tuples to a list of strings using map function.
    Original list of tuples:
    [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
	
    Convert the said list of tuples to a list of strings:
    ['red pink', 'white black', 'orange green']
12. Write a generator function which takes an integer n as a parameter. The function should return a generator which counts down from n to 0. Test your function using a for loop.
13. Write an “abstract” class, Box, and use it to define some methods which any box object should have: 
    a. add, for adding any number of items to the box, 
    b. empty, for taking all the items out of the box and returning them as a list, and 
    c. count, for counting the items which are currently in the box. 
    d. Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects. 
    e. Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.
14. Commit code to the GIT

### DAY 4


1. Write a simple program which loops over a list of user data (tuples containing a username, email and age) and adds each user to a dictionary if the user is at least 16 years old. You do not need to store the age. Write a simple exception hierarchy which defines a different exception for each of these error conditions:
	b. the age is not a positive integer
	c. the user is under 16
	d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
	e. Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move onto the next set of data in the list. Print a different error message for each different kind of exception.

2. Design simple calculater application where user input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

	a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
	b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
	c. If the second input is not '+' or '-', again raise a FormulaError
	d. If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.
3. Write a Python program that takes a text file as input and returns the number of words of a given text file.
	Note: Some words can be separated by a comma with no space.
4. Write a Python program to remove newline characters from a file (multiple blank lines)
5. Write a Python program to copy the contents of a file to another file .( if file already exits then raise a exception and use input from user to create a new file with new name)
6. Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.()
7. A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#". 
	Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
	Example :
	If the file matter.txt has the following content stored in it :
	THE WORLD IS ROUND
	
8. Write a class to handle below exceptions
	a. ZeroDivisionError
	b. ImportError
	c. IndexError
	d. IndentationError
	e. ValueError
	f. Exception
	g. Raise any exception and handle it properly and use else, finally blocks to print something irrespective of exception
9. Commit code to the repository

