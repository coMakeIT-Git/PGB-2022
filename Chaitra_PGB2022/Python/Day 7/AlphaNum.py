
l = list(input("Enter a string: ").split())
res = []
flag1 = False
flag2 = False

for str in l:
    flag1 = False
    flag2 = False
    for c in str:
        if (c.isalpha()):
            flag1 = True
        if(c.isdigit()):
            flag2 = True
        if(flag1 and flag2):
            res.append(str)
            break
print(res)