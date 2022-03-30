#Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
#Original dictionary of lists:
#{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
#Split said dictionary of lists into list of dictionaries:	
#[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language':80}]
def dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Original dictionary of lists:",marks)
print("\nAfter splitting:",dicts(marks))

#Write a Python program to convert a given list of tuples to a list of strings using map function.
#Original list of tuples:
#[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
#Convert the said list of tuples to a list of strings:
#['red pink', 'white black', 'orange green']

def tuples_string(lst):
    result = list(map(' '.join, lst))
    return result   
colors = [('black', 'white'), ('blue', 'purple'), ('orange', 'green')]
print("Original list of tuples:",colors)
print("\nAfter converting list of tuples to list of strings:",tuples_string(colors))



