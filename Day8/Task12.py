"""Write a Python program to sort a list of tuples using Lambda.
	Original list of tuples:
	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
	Sorting the List of Tuples:
	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]"""
li=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("original list :\n",li)
li.sort(key=lambda i:i[1])
print("After sorting using lambda function :\n",li)