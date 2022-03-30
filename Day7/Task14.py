#Write a program to remove special symbols / punctuation from a string
	#Ex : str1 = "/*We are le@arning python@67 fun_da**mentals**"
	#Output: We are learning python fundamentals
import string 
sentence =input("enter string")
no_punc_txt = ""
for char in sentence:
   if char not in string.punctuation:
       no_punc_txt = no_punc_txt + char
print(no_punc_txt); 