from itertools import combinations

l = list(map(int, input("Enter numbers: ").split()))
print("Input: ", l)
l = list(set(l))

allSets = []
result = []
sets = combinations(l,3)
for e in list(sets):
    allSets.append(list(e))

for e in allSets:
    if (e[0] + e[1] + e[2] == 0):
        result.append(e)

print("\nSets of 3 numbers which sum to 0:")
print(result)
