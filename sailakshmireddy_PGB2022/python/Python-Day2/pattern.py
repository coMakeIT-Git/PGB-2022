#Write a program to use for loop to print the following reverse number pattern
a=5
for x in range(0,a+1):
    for y in range(a-x,0,-1):
        print(y,end=" ")
    print()

