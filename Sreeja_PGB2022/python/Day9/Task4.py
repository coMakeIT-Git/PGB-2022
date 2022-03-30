filename="Day9/file1.txt"
flist = open(filename).readlines()
data=[s.rstrip('\n') for s in flist]
print(data)
