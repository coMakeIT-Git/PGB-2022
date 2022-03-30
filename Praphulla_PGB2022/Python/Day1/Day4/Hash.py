def hash_display():
    print("\n *Inside hash_display method*")
    f1 = open("hash_file.txt", "r")
    print(f1)
    content = f1.read()
    print("\t", content)
    print("\n **After adding of Hash symbols**")
    for character in content:
        print(character, end="#")
        f1.close()
hash_display()