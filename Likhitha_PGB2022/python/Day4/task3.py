#Write a Python program that takes a text file as input and returns the number of words of a given text file.
#Some words can be separated by a comma with no space.
from importlib.resources import path
import os.path

def countwords(filepath):
    with open(filepath) as f:
        d=f.read()
        d.replace(",", " ")
        return len(d.split(" "))
    
print(countwords("/home/localadmin/Desktop/words.txt"))
                   
 
 #Write a Python program to remove newline characters from a file
 
def removenewlines(filepath):
     flist=open(filepath).readlines()
     return [s.rstrip('\n') for s in flist]
 
print(removenewlines("/home/localadmin/Desktop/words.txt"))


#a Python program to copy the contents of a file to another file 

if os.path.isfile('home/localadmin/Desktop/testfile.txt'):
    print ("File exist")
else:
    print ("File not exist")
    with open('/home/localadmin/Desktop/words.txt','r') as firstfile, open('/home/localadmin/Desktop/testfile.txt','w') as secondfile:
      
    # read content from first file
        for line in firstfile:
               
             # write content to second file
             secondfile.write(line)   
             
             
#A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#". 
	#Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
	#Example :
	#If the file matter.txt has the following content stored in it :
	#THE WORLD IS ROUND
 
 
def counthash():
    file=open('/home/localadmin/Desktop/words.txt') 
    d=file.read()
    
    for i in d:
        print(i,end='#')
        
    file.close()
    
counthash()
    
	               