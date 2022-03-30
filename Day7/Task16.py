#Write a program to find words with both alphabets and numbers from an input string.
	#Input : str1 = "Sriman25 is Data scientist50 and AI Expert"
	#Output : ['Sriman25','Scientist50']
inp=input("enter a string with alphabest and numbers")
res = []
temp = inp.split()
for idx in temp:
    if any(chr.isalpha() for chr in idx) and any(chr.isdigit() for chr in idx):
        res.append(idx)
print("Words with alphabets and numbers : " + str(res)) 