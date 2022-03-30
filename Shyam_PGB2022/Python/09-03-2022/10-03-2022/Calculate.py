def calculation(a, b):
    sumx = a + b
    suby = a - b
    return sumx, suby


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    result = calculation(a, b)
    print("THe result is:", result)
