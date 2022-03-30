"""Write a Python program to convert a given list of tuples to a list of strings using map function.
	Original list of tuples:
	[('red', 'pink'), ('white', 'black'), ('orange', 'green')]"""
listA = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list : \n", listA)
res = list(map(''.join, listA))
print("list of tuples to a list of strings using map function: \n",res)