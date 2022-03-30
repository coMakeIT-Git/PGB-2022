print("\n Enter the name of the Source File: ", end="")
s = input()
#Handling IO Exceptions
try:
    filehandle = open(s, "r")
    print("\n Enter the name of the Target File: ", end="")
    t = input()
    texts = filehandle.readlines()
    filehandle.close()

    try:
        filehandle = open(t, "w")
        for s in texts:
            filehandle.write(s)
        filehandle.close()

        print("\n Content of \"" +s+ "\" gets Copied to \"" +t+ "\" Successfully!")
        print("\n Displaying contents of the file" +t,"\t",end="")
        try:
                filehandle = open(t, "r")
                contents = filehandle.readlines()
                for s in contents:
                    print(s, end="")
                filehandle.close()
                print()
        except IOError:
            print("\n Error occurred while opening the file!")

    except IOError:
        print("\n Error occurred while opening/creating the file!")

except IOError:
    print("\n The file doesn't exist!")