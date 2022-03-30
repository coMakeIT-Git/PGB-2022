

d = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
#print(d["Science"][0])
result = map(dict, zip(*[[(key, val) for val in value] for key, value in d.items()]))
print(list(result))



