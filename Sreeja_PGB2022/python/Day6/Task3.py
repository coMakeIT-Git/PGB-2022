name="i am Kotagiri Sreeja"
x="INDIA"
print("converting the name to uppercase",name.upper())
print("converting the name to lowercase",name.lower())
print("count of specific value",name.count("i"))
print("checking the string ends with Sreeja value ",name.endswith("Sreeja"))
print("return true if all the letters in the string are alphabets",name.isalpha())
print("return true if all the letters in the string are alphabets",x.isalpha())
print("converting the first letter of each word to uppercase",name.title())
print("converting only the first letter of first word to uppercase",name[0].upper() + name[1:])
print("finding the position of specified string",name.find("Sreeja"))
print("reversing the string using slicing")
stringlength=len(name) # calculate length of the list
slicedString=name[stringlength::-1] # slicing 
print (slicedString) # print the reversed string

print("creating tuple")
a = ("apple", "banana", "cherry","mango","pine apple","apple") 
print("Tuple is",a)	 
print("Number of times the apple occured is ",a.count("apple"))
print("index at which mango occured is ",a.index("mango"))