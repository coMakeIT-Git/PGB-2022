"""Write a generator function which takes an integer n as a parameter. The function should return a generator which counts down from n to 0. Test your function using a for loop."""

def infinite_sequence():
    nums=4
    while (nums>=0):
        yield nums
        nums -=1
for i in infinite_sequence():
    print(i, end=" ")