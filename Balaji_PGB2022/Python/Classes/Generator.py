def generator_func(n):
    while(n>=1):
        yield n
        n-=1
n=int(input("Enter n value:"))
for i in generator_func(n):
    print(i)