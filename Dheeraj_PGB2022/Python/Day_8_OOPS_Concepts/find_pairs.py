# 8. Write a Python class to get all possible unique subsets from a set of distinct integers.
# 	Input : [4, 5, 6]
# 	Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

class GetSets:
    def __init__(self, subset):
        self.subset = subset
        print(self.get_sets())

    def get_sets(self):
        return self.unique_sets([], sorted(self.subset))

    def unique_sets(self, current, subset):
        if subset:
            # print(current, subset[0], subset[1:])
            return self.unique_sets(current, subset[1:]) + self.unique_sets(current + [subset[0]], subset[1:])
        return [current]


run = GetSets([4, 5, 6])


# 9. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
# 	Note: Do not use the same element twice.
# 	Input: numbers= [10,20,10,40,50,60,70], target=50
# 	Output: 3, 4

class FindTwoPair:
    def __init__(self, lst, target):
        print(self.getPair(lst, target))

    def getPair(self, lst, target):
        i1, i2 = -1, -1
        for i, num in enumerate(lst):
            if (target - num) in lst:
                i1, i2 = i, lst.index(target - num)
            lst[i1] = i2
        return i1+1, i2+1


run = FindTwoPair([10, 20, 10, 40, 50, 60, 70], 50)


# 10. Write a Python class to find the three elements that sum to zero from a set of n real numbers.
# 	Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# 	Output : [[-10, 2, 8], [-7, -3, 10]]

class FindThreePair:
    def __init__(self, n_list):
        self.ans = []
        print(self.pair(n_list))

    def pair(self, n_list):
        n = len(n_list)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if n_list[i] + n_list[j] + n_list[k] == 0:
                        self.ans.append([n_list[i], n_list[j], n_list[k]])
        return self.ans


FindThreePair([-25, -10, -7, -3, 2, 4, 8, 10])
