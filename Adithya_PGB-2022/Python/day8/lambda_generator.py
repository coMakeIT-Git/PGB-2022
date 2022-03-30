t1=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lambda_func=sorted(t1,key=lambda x:len(x[0]))
print(lambda_func)
d=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
lambda_func=sorted(d,key=lambda x:x['color'])
print(lambda_func)
test_dict={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
res = [{key : value[i] for key, value in test_dict.items()}
         for i in range(2)]
print ("The converted list of dictionaries " +  str(res))
l=[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
lambda_func=list(map(lambda x: x[0]+" "+x[1],l)) 
print(lambda_func)


def generator(n):
	if(n==0):
		return 0
	for i in range(n,0,-1):
		yield i
for i in generator(10):
	print(i)

