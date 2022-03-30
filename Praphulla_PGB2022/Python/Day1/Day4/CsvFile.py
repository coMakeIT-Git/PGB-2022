f1 = open("data.csv", 'r')
content = f1.readlines()
content = content[1:]
print(content)
f1.close()


