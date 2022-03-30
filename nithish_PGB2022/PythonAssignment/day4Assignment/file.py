
def word_count(file):
    with open(file) as f:
        data=f.read()
        data.replace(","," ")
        return len(data.split(" "))

print("no of words in text file: ",word_count("sample.txt"))

#--------------------------------------------------------------------------------------

def remove_newlines(file):
    with open(file) as f:
        data=f.readlines()
    return [i.rstrip('\n') for i in data]

print("removes newlines in file: ",remove_newlines("sample.txt"))

#--------------------------------------------------------------------------------------

def copy_file(file):
    with open(file,'r') as f1,open('copy.txt','w') as f2:
        for line in f1:
            f2.write(line)

print("file copy done")
copy_file("sample.txt")


#---------------------------------------------------------------------------------------

import csv
fields=[]
rows=[]
with open('color.csv') as f:
    data=csv.reader(f)
    fields=next(data)
    for row in data:
        print(', '.join(row))
print("No. of rows: ",data.line_num)
print('Field names are:')
print(', '.join(field for field in fields))
