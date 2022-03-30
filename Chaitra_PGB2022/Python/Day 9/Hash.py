def hash_display(f):
    for c in f.read():
        print(c, end="#")

Name = input("Enter File Name: ")
path = "Files/" + Name
f = open(path, 'r')
hash_display(f)

