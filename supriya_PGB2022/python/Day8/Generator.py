#Write a generator function which takes an integer n as a parameter. 
# The function should return a generator which counts down from n to 0. Test your function using a for loop.
def Generator(n):
    while(n>=0):
        yield n
        n-=1
for i in Generator(6):
    print(i)