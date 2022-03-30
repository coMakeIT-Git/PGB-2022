#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result. 
s1 = input("Enter the string1:")
s2 = input("Enter the string2:")
len1 = len(s1)
len2= len(s2)
length = len1 if len1 > len2 else len2
s3 = ""
s2 = s2[::-1]


for i in range(length):
    if i < len1:
        s3 = s3 + s1[i]
    if i < len2:
        s3 = s3+ s2[i]

print("string3: " +s3)