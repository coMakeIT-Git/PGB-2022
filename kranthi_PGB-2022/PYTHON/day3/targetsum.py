#a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.

class tsum:
    def indexsums(l,n):
        for i in range (len(l)):
            for j in range(len(l)):
                if(l[i]+l[j]==n):
                    return (i,j)
li=[10,20,10,30,40, 50,60,20]
n=50

print(" Indices of elements whose sum is target value:")
print(tsum.indexsums(li,n))
