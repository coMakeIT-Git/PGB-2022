class ContentAlreadyAvailable(Exception):
    pass


def wordscount(file):
    f1 = open(file)
    content = f1.read()
    content.replace(",", " ")
    return len(content.split(" "))


print(wordscount("txtdemo"))


def newline(file):
    f1 = open(file).readlines()
    return [s.rstrip('\n') for s in f1]


print(newline("txtdemo"))

from shutil import copyfile

f1 = open("txtdemo", 'r')
char = f1.read(1)
try:
    if not char:
        raise ContentAlreadyAvailable()
        print("No")
except ContentAlreadyAvailable():
    print("Can't get copied")
else:
    copyfile('txtdemo', 'abc.py')
    print("Yes")


    fields = ['Name', 'Age', 'Location']

rows = [ ['Shyam','21', 'Vizag'],
		['Vihaan', '6', 'Hyderabad'],
		['Nikhil', '16', 'Vizag'],
		['Bhuvana', '14', 'Purushothapuram'],
		]

with open('familyxyz.csv', 'w') as csvfile:

	csvwriter = csv.writer(csvfile)

	csvwriter.writerow(fields)
		
	csvwriter.writerows(rows)



f1 = open("familyxyz.csv", 'r')


content = f1.readlines()
content = content[1:]
print(content)
f1.close()


def EndWithHash():
    f1 = open("txtdemo", "r")
    content = f1.read()
    for character in content:
        print(character, end="#")
    f1.close()


EndWithHash()

