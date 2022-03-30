from os.path import exists

try:
    Name1 = input("Enter Source File Name: ")
    path = "Files/" + Name1
    f1 = open(path, 'r')

    Name2 = input("Enter Destination File Name: ")
    path = "Files/" + Name2
    while(exists(path)):
        c = input("\nThe file already exists. \nDo you want to replace it (y/n)?: ")
        if(c=="y"):
            break
        elif (c == "n"):
            Name2 = input("\nEnter New Destination File Name: ")
            path = "Files/" + Name2

    f2 = open(path, 'w+')
    for line in f1.read():
        f2.write(line)
    print("Copied successfully!")


except FileNotFoundError:
    print("Error: The Source File does not exist.")


