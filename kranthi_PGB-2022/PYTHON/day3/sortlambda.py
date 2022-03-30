"""Write a Python program to sort a list of tuples using Lambda.
	Original list of tuples:
	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
	Sorting the List of Tuples:
	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

"""



person_ages = [('kranthi', 21), ('raju', 20), ('manasa', 18), ('Swetha', 15)]
print("Sorting using Lambda expression:")
print("Original list of tuples:")
print(person_ages)
person_ages.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(person_ages)