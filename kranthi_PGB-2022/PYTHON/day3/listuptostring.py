"""Write a Python program to convert a given list of tuples to a list of strings using map function.
	Original list of tuples:
	[('red', 'pink'), ('white', 'black'), ('orange', 'green')]

	Convert the said list of tuples to a list of strings:
	['red pink', 'white black', 'orange green']


"""
def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples:")
print(colors)
print("\nConvert the said list of tuples to a list of strings:")
print(tuples_to_list_string(colors))