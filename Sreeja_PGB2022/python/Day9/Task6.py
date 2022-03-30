import csv
fields = []
rows = []
with open('Day9/file.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar=',')

 fields = next(data)
 for row in data:
   print(', '.join(row))
print("\nTotal no. of rows: %d"%(data.line_num))
print('Field names are:')
print(', '.join(field for field in fields))