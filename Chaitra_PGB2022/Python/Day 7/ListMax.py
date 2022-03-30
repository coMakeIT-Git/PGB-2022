l = list(map(int, input("Enter a list: ").split()))
max = l[0]
for e in l:
    if e > max:
        max = e
print("Maximum value:", max)
