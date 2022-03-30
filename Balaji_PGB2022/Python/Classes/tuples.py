#sort a list of tuples using Lambda
lst=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst.sort(key=lambda y:y[1])
print("After sorting the list are:")
print(lst)

#list of dictionaries by color using Lambda
lst=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
lst.sort(key=lambda y:y['color'])
print("After sorting list based on colour:")
print(lst)


#dictionary of lists into list of dictionaries
def func(d):
    result = map(dict, zip(*[[(k, v) for v in value] for k, value in d.items()]))
    return list(result)
dictionary={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Original dictionary of lists are :")
print(dictionary)
print("convert the dictionary of lists to list of dictionary")
print(func(dictionary))

#list of tuples to a list of strings
def function(l):
    result=list(map(' '.join, l))
    return result
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples are :")
print(colors)
print("Convert the list of tuples to a list of strings:")
print(function(colors))



