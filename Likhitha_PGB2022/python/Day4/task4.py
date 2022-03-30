import csv

fields=[]
rows=[]

with open('Day4/employees.csv',newline='') as csvfile:
    data=csv.reader(csvfile,delimiter =' ', quotechar=',')
    
    fields=next(data)
    
    for r in data:
        print(', '.join(r))
        
print("Number of rows: ",data.line_num)
print("Field names are: ")
print(", ".join(s for s in fields))
    
    