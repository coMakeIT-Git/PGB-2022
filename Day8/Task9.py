 #Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
	#Note: Do not use the same element twice.
	#Input: numbers= [10,20,10,40,50,60,70], target=50
	#Output: 3, 4"""



class Pair:
    def chkPair(lst,target) :
        for i in range ( 1,len(lst) - 1) :
            for j in range (i + 1, len(lst)):
                if (lst[i] + lst[j] == target) :
                    print(i,j)
lst = list(map(int, input("Type number with space: ").split()))
target=int(input("enter target"))
Pair.chkPair(lst,target)
