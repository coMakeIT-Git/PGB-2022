import csv

file = open("Files/username.csv")
csvreader = csv.reader(file)
header = next(csvreader)

count = 0
for row in csvreader:
    count+=1

print("Number of rows: ", count)

print("\n***Fields***")
print(header[0].split(";"))
