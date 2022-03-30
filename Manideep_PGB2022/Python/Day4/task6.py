# A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#". 
# 	Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
# 	Example :
# 	If the file matter.txt has the following content stored in it :
# 	THE WORLD IS ROUND



f=open('Day4/matter.txt','r')

data=f.read()
for i in data:
    print(i,end='#')
f.close()