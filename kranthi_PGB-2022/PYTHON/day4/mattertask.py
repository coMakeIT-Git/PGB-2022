'''
A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#".
	Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
	Example :
	If the file matter.txt has the following content stored in it :
	THE WORLD IS ROUND
'''

print("A progrom to insert hash")
def insert_hash():
    with open("matter.txt","r") as file:
        dt = file.read()
        for ch in dt:
            print(ch, end="#")
    print()

insert_hash()



