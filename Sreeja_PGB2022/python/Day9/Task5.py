import os.path

print(os.getcwd())
f= open("Day9/out1.txt","w+")

if not os.path.isfile('Day9/out1.txt'):
    print ("invalid")
else:
    print("valid")
    with open("Day9/file1.txt") as f:
        with open("Day9/out1.txt", "w") as f1:
            for line in f:
                f1.write(line)
