def pattern(x):
	a=x
	for i in range(a):
		y=x
		for j in range(x):
			print(y,end=" ")
			y=y-1
		print()
		x=x-1
def count(s):
	alpha=0
	num=0
	special=0
	for i in s:
		if(i.isalpha()):
			alpha+=1
		elif(i.isdigit()):
			num+=1
		else:
			special+=1
	return alpha,num,special
def func(s1,s2):
	s3=""
	p1=0
	p2=len(s2)-1
	while(p1<len(s1)and p2>=0):
		s3+=s1[p1]+s2[p2]
		p1+=1
		p2-=1
	while(p1<len(s1)):
		s3+=s1[p1]
		p1+=1
	while(p2>=0):
		s3+=s2[p2]
		p2-=1
	print("result string: ",s3)
def remove_special_symbols(s):
	s1=""
	for i in s:
		if i.isalpha() or i.isspace():
			s1+=i
	print("result string after removing special symbols: ",s1)
def remove_all_characters(s):
	s1=""
	for i in s:
		if i.isdigit():
			s1+=i
	print("result string after removal of all characters from a string except integers: ",s1)
def check(s):
	a=b=0
	for i in s:
		if i.isalpha():
			a+=1
		elif i.isdigit():
			b+=1
	if(a>=1 and b>=1):
		return True
	return False
def find_pattern(s):
	s=s.split()
	l=[]
	for i in s:
		alpha,digit,special=count(i)
		if(alpha>0 and digit>0):
			if(special==0):
				l.append(i)
	print("result list after finding both aplhabets and numbers from string: ",l)
#reverse number pattern
pattern(5)
#Count of all letters, digits, and special symbols from a given string
print("Count of alpha,digit,special characters: ",count("Adithya1@"))
#s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result
func("adithya","raviteja")
#remove special symbols / punctuation from a string
remove_special_symbols("/*We are le@arning python@67 fun_da**mentals**")
#removal all characters from a string except integers
remove_all_characters("I am 20 years and and 22 months old")
#list of words with both alphabets and numbers from an input string
find_pattern("Sriman25 is Data scientist50 and AI Expert")
