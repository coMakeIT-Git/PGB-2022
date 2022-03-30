"""Write a Python program that takes a text file as input and returns the number of words of a given text file.
	Note: Some words can be separated by a comma with no space."""
    
count=0      
file = open("file1.txt", "r")            
for line in file:  
    words = line.split(" ");  
    count = count + len(words);  
       
print("Number of words present in given file: " + str(count));  
file.close();  

""" Write a Python program to remove newline characters from a file"""
givenFilename = "file1.txt"
with open(givenFilename, 'r') as givenfilecontent:
    lines_lst= givenfilecontent.readlines()
    print([a.rstrip('\n') for a in lines_lst])

"""Write a Python program to copy the contents of a file to another file ."""
import os.path

file_exists = os.path.exists('pp.txt')
if(file_exists):
    print("file already exists")
else:
    with open('file1.txt','r') as f1:
        with open('filess.txt','w+') as f2:
            for l in f1:
                f2.write(l)
"""A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#". 
	Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
	Example :
	If the file matter.txt has the following content stored in it :
	THE WORLD IS ROUND"""
def hash_display():
    with open('matter.txt','r') as f:
        data=f.read()
        for l in data:
            print(l,end="#")
hash_display()
    

