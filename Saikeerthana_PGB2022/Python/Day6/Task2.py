import string
str="nalla saikeerthana"
print("Converted to uppercase:",str.upper())
print("Converted to lowecase:",str.lower())

substr = 'sai'

# Occurences of substring 'apples' in the string
result = str.count(substr)
print("Number of substring occurrences:", result)
print("String ends with a:",str.endswith("a"))
print("Converting first letter of each word to uppercase:",string.capwords(str))
res = str[0].upper() + str[1:]
print("Convertuing first character to capital letter:",res)
print("Character a occured at :",str.find("s"),"position")
print("Reverse string using slicing:",str[::-1])