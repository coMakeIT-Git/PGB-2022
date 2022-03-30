subject_vs_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_vs_marks)
subject_vs_marks.sort(key=lambda a: a[1])
print("\nSorting the List of Tuples:")
print(subject_vs_marks)
devices = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(devices)
sort_devices = sorted(devices, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sort_devices)
def dict_pairs(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
mappedto = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Original dictionary of lists:")
print(mappedto)
print("\nSplit said dictionary of lists into list of dictionaries:")
print(dict_pairs(mappedto))
def intostring(nlist):
    outcome = list(map(' '.join, nlist))
    return outcome
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples:")
print(colors)
print("\nConvert the said list of tuples to a list of strings:")
print(intostring(colors))