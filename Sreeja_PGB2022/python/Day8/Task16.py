def my_gen(num):
    while(num>=0):
        yield num
        num-=1

# Using for loop
for i in my_gen(5):
    print(i)