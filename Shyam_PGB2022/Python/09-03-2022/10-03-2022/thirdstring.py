s1 = "Shy"
s2 = "rap"
s3 = ""
for i in range(len(s1)):
    s3+=s1[i]
    s3+=s2[-i-1]
print(s3)