#Write a program to removal all characters from a string except integers
	#Input : str1 = 'I am 20 years and and 22 months old'
	#Output : 2022
inp=input("enter an input string")
temp=filter(str.isdigit,inp)
result="".join(temp)
print(result)