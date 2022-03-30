import csv
# Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.
with open("new.csv","r") as file1:
    csvFile = csv.reader(file1,delimiter = ',')
    field=[]
    header=next(csvFile)
    c=0
    for lines in csvFile:
        print(lines)
        c=c+1
    for row in header:
        field.append(row)
    print("The field names are:",field)
    print("the number of rows without header:",c)
print("***********")