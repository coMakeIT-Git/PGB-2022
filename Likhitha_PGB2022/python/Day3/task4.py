
#a Python class to get all possible unique subsets from a set of distinct integers

class Subset():
    def func1(self,s1):
        return self.func2([],sorted(s1))
    
    def func2(self,curr,s1):
        if s1:
            return self.func2(curr,s1[1:])+self.func2(curr+[s1[0]],s1[1:])
        return [curr]
    

n=int(input("Enter size of array :"))
a=[]

for i in range(n):
    b=int(input("Enter value : "))
    a.append(b)
    
print("Subsets: ")
print(Subset().func1(a))