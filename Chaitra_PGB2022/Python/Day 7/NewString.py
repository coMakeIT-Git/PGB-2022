str1 = input("Enter String 1: ")
str2 = input("Enter String 2: ")

print("String 1: ", str1, "\nString 2: ", str2)

l = len(str1) if len(str1) <= len(str2) else len(str2)

if len(str1) <= len(str2):
    s1 = str2
    s2 = str1
else:
    s2 = str2
    s1 = str1

NewString = ""
for i in range(l):
    NewString += s1[i]
    NewString += s2[l-i-1]
for c in range(l,len(s1)):
    NewString += s1[c]

print("New String: ", NewString)


