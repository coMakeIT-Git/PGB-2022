#sort a list of tuples using Lambda
lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst = sorted(lst, key=lambda y:y[1])
print(lst)
print()

#sort a list of dictionaries by color using Lambda
l2 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
l2 = sorted(l2, key=lambda x:x['color'])
print(l2)
print()

#split a given dictionary of lists into list of dictionaries using map
d = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
p = list(map(dict, zip(*[[(k, v) for v in value] for k, value in d.items()])))
print(p)
print()

#-------------------------------------------------------------------------------------------------------------------
#convert a given list of tuples to a list of strings using map function
s = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
res = list(map(' '.join,s))
print(res)