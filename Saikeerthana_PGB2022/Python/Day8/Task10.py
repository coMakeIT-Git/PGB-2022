"""Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
	Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
	Output : [[-10, 2, 8], [-7, -3, 10]]"""
class Sum:
    def vtriplets(lst):
        for i in range(len(lst)-2):
            for j in range(i+1,len(lst)-1):
                for k in range(j+1,len(lst)):
                    if(lst[i]+lst[j]+lst[k]==0):
                        print([lst[i],lst[j],lst[k]])
lst = list(map(int, input("Type number with space: ").split()))
Sum.vtriplets(lst)


