str = input("Enter input string :")

punc='''~!@#$%^&*()_+{}:""[]|-+,./<>?='''

res=""
for char in str:
    if char not in punc:
        res=res+char
     
print("String after removing punctuations: ",res)     