def count_hash():
    file = open("Day9/file1.txt","r")
    data = file.read()
    for character in data:
        print(character, end="#")

    file.close()

count_hash()
