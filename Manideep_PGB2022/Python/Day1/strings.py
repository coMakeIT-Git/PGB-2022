# a. Convert it into upper case
# 	b. Convert into lower case
# 	c. Return the number of times a specified value occurs in a string
# 	d. Return true if the string ends with the specified value
# 	e. Return True if all characters in the string are in the alphabet
# 	f. Convert the first character of each word to upper case
# 	g. Convert the first character to upper case
# 	h. Search the string for a specified value and returns the position of where it was found
# 	i. Reverse the string with slicing

s='welcome to ComakeIt'
s=s.upper()
print(s)
s=s.lower()
print(s)

print('Enter a specific character to find no of times it got occured')
k=input()
print(s.count(k))

print('Enter a specific character to check whether string ends with specified character or not')
k=input()
print(s.endswith(k))

print('Checking all characters are there or not')
print(len(set(s))==26)

#convert the first character of each word to upper case

k=s.split()
for i in range(len(k)):
    k[i]=k[i].capitalize()
s=' '.join(k)
print(s)
# Convert first character to upper case
print(s.capitalize())
#Search the string for a specified value and returns the position of where it was found
print(s.find('c'))
s=s[::-1]
print(s)

