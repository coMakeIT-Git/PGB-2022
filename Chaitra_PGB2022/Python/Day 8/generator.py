def CountDown(n):
    while n >= 0:
        yield n
        n -= 1

print("***Countdown***")
for i in CountDown(5):
    print(i)