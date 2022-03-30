#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def sum(num):
    if(num<=1):
        return num
    else:
        return num+sum(num-1)
num=10
print("sum of numbers is:",sum(num))