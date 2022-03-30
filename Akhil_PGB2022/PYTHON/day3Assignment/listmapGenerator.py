#sort a list of tuples using Lambda
lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst = sorted(lst, key=lambda y:y[1])
print(lst)


#sort a list of dictionaries by color using Lambda
l2 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
l2 = sorted(l2, key=lambda x:x['color'])
print(l2)


#split a given dictionary of lists into list of dictionaries using map
d = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
p = list(map(dict, zip(*[[(k, v) for v in value] for k, value in d.items()])))
print(p)


#convert a given list of tuples to a list of strings using map function
s = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
res = list(map(' '.join,s))
print(res)


#Generator function
def genFunc(n):
	for i in range(n,0,-1):
		yield i

for i in genFunc(20):
	print(i)







'''
class real_nums:
    def pairs(self,lst):
        b=[]
        for x in lst:
            for y in lst:
                for z in lst:
                    c = []
                    if(x+y+z==0):
                        c=c+[x]+[y]+[z]
                        c=sorted(c)
                        b.append(c)
        d=[]
        for x in b:
            if x not in d:
                d.append(x)
        return d
obj=real_nums().pairs( [-25, -10, -7, -3, 2, 4, 8, 10])
print(obj)
'''









