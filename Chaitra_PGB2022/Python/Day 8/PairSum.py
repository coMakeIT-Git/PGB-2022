from itertools import combinations

l = list(map(int, input("Enter numbers: ").split()))
print("Input: ", l)
copy = l
l = list(set(l))

total = int(input("Enter Sum: "))
allSets = []
result = []
sets = combinations(l,2)
for e in list(sets):
    allSets.append(list(e))

for e in allSets:
    if (e[0] + e[1] == total):
        result.append(e)

print("\nPositions of numbers who sum equals ", total, ":")
for e in result:
    print(copy.index(e[0])+1, copy.index(e[1])+1, sep=",")

