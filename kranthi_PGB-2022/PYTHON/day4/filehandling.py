f= open('kranthi.txt','w')
f.write('This is my file to count numbers of words in it \n')
with open('kranthi.txt') as f:
    data=f.read()
data.replace(","," ") #Replaces all the comas with space

print("The number of words in the sentence of the file are:")
print(len(data.split(" "))) #Converting sentence in to words using split and printing the count

with open('kranthi.txt','a') as k:
    k.write("This is a new line kranthi \n")
    k.write("This is the third  line kranthi \n")
    k.write("I am keep on writing my fourth line yaar")

#Write a Python program to remove newline characters from a file
print("a Python program to remove newline characters from a file \n")
def remove(filename):
    f3 = open(filename).readlines()
    return [s.rstrip('\n') for s in f3]
print(remove('kranthi.txt'))

# Write a Python program to copy the contents of a file to another file .
print("a Python program to copy the contents of a file to another file .")
with open('kranthi.txt','r') as f1, open('file2.txt','a') as f2:
    for line in f1:
        f2.write(line)

with open('file2.txt','r') as fr:
    data1=fr.read()
    print(data1)
print('\t')

