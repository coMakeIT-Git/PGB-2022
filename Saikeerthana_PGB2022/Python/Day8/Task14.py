"""Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
	Original dictionary of lists:
	{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
	Split said dictionary of lists into list of dictionaries:	
	[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language':80}]"""
dic={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("original list :\n",dic)
res=map(dict, zip(*[[(k, v) for v in value] for k, value in dic.items()]))
print(list(res))