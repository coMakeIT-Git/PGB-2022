def listMax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max
list1 = [5,44,56, 16,72]
print("Largest element is:",listMax(list1))