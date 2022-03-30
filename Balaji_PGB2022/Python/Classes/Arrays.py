#array whose sum equals a specific target number.
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

#all possible unique subsets from a set of distinct integers.
class solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]


print(solution().sub_sets([4, 5, 6]))


#find the three elements that sum to zero
class solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))