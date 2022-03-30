#Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
	#Note: Do not use the same element twice.
	#Input: numbers= [10,20,10,40,50,60,70], target=50
	#Output: 3, 4

class add_target:
    def sum(nums,target):
        ind={}
        for i,n in enumerate(nums):
            if target - n in ind:
               return (ind[target - n], i )
            ind[n] = i
print("index is: %d,%d" %add_target.sum([10,20,40,50,60,70],50))
