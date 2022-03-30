#TASK7


#Convert STRING into upper case
str1 = "sai sowmya"
print(str1.upper())

#Convert STRING into LOWER case
str1 = "HELLOWORLD"
print(str1.lower())

# Return the number of times a specified value occurs in a string
x = str1.count("L")
print(x) 


#Return true if the string ends with the specified value
print(str1.endswith('D'))

#Return True if all characters in the string are in the alphabet
print(str1.isalpha())

#Convert the first character of each word to upper case
str2 = "hello world sowmya"
conv_first_letter=str2.title()
print(conv_first_letter)

#Convert the first character to upper case
str2 = "hello world"
print(str2.capitalize())

#Search the string for a specified value and returns the position of where it was found
print(str2.find("w"))

#Reverse the string with slicing
txt = "Hello World" [::-1]
print(txt) 