rows = 5
print("\n Reverse Triangular Pattern:")
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()