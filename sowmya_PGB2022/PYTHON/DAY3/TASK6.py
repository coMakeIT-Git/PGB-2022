import itertools
stuff = list(map(int, input("Type number with space: ").split()))
stuff.sort()
ls = []
for subset in itertools.combinations(stuff, 3):
    if sum(list(subset))==0:
        if list(subset) not in ls:
            ls.append(list(subset))
print(ls)
#[-25, -10, -7, -3, 2, 4, 8, 10]