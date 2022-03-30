
class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6]))

def check():
	l=[20,25,32,4,2,5]
	n=[]
	target=6
	for i in l:
		n.append(target-i)
	for i in range(0,len(n)):
		if n[i] in l:
			return i,l.index(n[i])
	return -1,-1
print(check())

class student:
	pass
class Marks:
	pass
a=student()
print(type(a),isinstance(a,student))
b=Marks()
print(isinstance(b,object))

