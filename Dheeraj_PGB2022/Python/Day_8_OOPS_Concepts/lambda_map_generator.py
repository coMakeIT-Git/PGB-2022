# 12. Write a Python program to sort a list of tuples using Lambda.
# 	Original list of tuples:
# 	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# 	Sorting the List of Tuples:
# 	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

def sort_tuple(tup):
    return sorted(tup, key=lambda x: (x[1], x[0]))


s = sort_tuple([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
print(s)


# 13. Write a Python program to sort a list of dictionaries by color using Lambda.
# 	Original list of dictionaries :
# 	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# 	Sorting the List of dictionaries :
# 	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
def sort_dict(dit):
    return sorted(dit, key=lambda x: x["color"])


t = sort_dict([{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}])
print(t)


# 14. Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
# 	Original dictionary of lists:
# 	{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# 	Split said dictionary of lists into list of dictionaries:
# 	[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language':80}]

def dl_to_ld(DL):
    return [dict(map(lambda x, y: [x, y], DL, val)) for val in zip(*DL.values())]


dit = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(dl_to_ld(dit))


# 15. Write a Python program to convert a given list of tuples to a list of strings using map function.
# 	Original list of tuples:
# 	[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
#
# 	Convert the said list of tuples to a list of strings:
# 	['red pink', 'white black', 'orange green']
def tl_to_lt(TL):
    return list(map(' '.join, TL))


dit = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(tl_to_lt(dit))


# 16. Write a generator function which takes an integer n as a parameter. The function should return a generator which counts down from n to 0. Test your function using a for loop.

def generator_func(n):
    for i in range(n, 0, -1):
        yield i


for j in generator_func(9):
    print(j)





