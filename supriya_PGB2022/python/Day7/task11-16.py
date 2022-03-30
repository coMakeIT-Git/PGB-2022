# Write a program to use for loop to print the following reverse number pattern
for j in range(5,0,-1):
	for i in range (j,0,-1):
		print(i,end= " ")
	print()
#Count all letters, digits, and special symbols from a given string
str = "tom@56&&589_*jerry!"
letters = digits = symbols = 0

for i in range(len(str)):
    if(str[i].isalpha()):
        letters = letters + 1
    elif(str[i].isdigit()):
        digits = digits + 1
    else:
        symbols = symbols + 1
        
print("\nTotal Number of Letters in this String :  ", letters)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Symbols Characters in this String :  ", symbols)	
#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, 
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. 
# Any leftover chars go at the end of the result.
s1 = "tom"
s2 = "cat"
s3=''
for i in range(len(s1)):
    s3+=s1[i]
    s3+=s2[-i-1]
print(s3)
#Write a program to remove special symbols / punctuation from a string
#Ex : str1 = "/*We are le@arning python@67 fun_da**mentals**"
#Output: We are learning python fundamentals
punc ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str="/*We are le@arning python@67 fun_da**mentals**"
no_punc = ""
for char in str:
    if char not in punc:
      no_punc = no_punc + char
result = ''.join([i for i in no_punc if not i.isdigit()])      
print (result)
# Write a program to removal all characters from a string except integers
#Input : str1 = 'I am 20 years and and 22 months old'
#Output : 2022
input = 'I am 20 years and and 22 months old'
output = ''.join(c for c in input if c.isdigit())
print(output) 
#Write a program to find words with both alphabets and numbers from an input string.
#Input : str1 = "Sriman25 is Data scientist50 and AI Expert"
#Output : ['Sriman25','Scientist50']
 
txt = "Sriman25 is Data scientist50 and AI Expert"
# Words with both alphabets and numbers
# Using isdigit() + isalpha() + any()
txt = ["Sriman25 is Data scientist50 and AI Expert"]
for i in txt:
    for x in i.split(' '):
        if x.isalnum() and not x.isalpha() and not x.isdigit():
            print (x)

