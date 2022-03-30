from itertools import combinations
l = list(map(int, input("Enter numbers: ").split()))
print("Input: ", l)
allSets = []
for n in range(len(l)+1):
    sets = combinations(l,n)
    for e in list(sets):
        allSets.append(list(e))

print(allSets)
