
#a Python class to get all possible unique subsets from a set of distinct integers.
def sub_lists(l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists



l1 = [4,5,6]
print("a Python class to get all possible unique subsets from a set of distinct integers.")

print(sub_lists(l1))