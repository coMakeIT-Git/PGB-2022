s1 = input("Enter the string1:")
s2 = input("Enter the string2:")

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
s3 = ""

# reverse s2
s2 = s2[::-1]

# iterate string 
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        s3 = s3 + s1[i]
    if i < s2_length:
        s3 = s3+ s2[i]

print("string3: " +s3)