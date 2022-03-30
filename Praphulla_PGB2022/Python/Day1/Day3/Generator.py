def numSequence():
    num = 10
    while num>=1:
        yield num
        num = num-1
    print(num)

for i in numSequence():
    print(i, end=" ")