def sequence():
    num = 10
    while num>=1:
        yield num
        num = num-1
    print(num)

for i in sequence():
    print(i, end=" ")