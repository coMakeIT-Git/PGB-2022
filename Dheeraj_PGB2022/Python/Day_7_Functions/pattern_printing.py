def print_pattern(n):
    for j in range(n, 0, -1):
        for i in range(j, 0, -1):
            print(i, end=" ")
        print()


print_pattern(5)
