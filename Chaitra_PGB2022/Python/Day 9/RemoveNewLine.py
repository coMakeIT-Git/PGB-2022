
Name = input("Enter File Name: ")
path = "Files/" + Name
f = open(path, 'r')

data = f.read()

print("\n***Old Data***")
print(data)
text = ''.join(data.splitlines())

print("\n***Updated Data***")
print(text)
#write data to file
#f.write(text)