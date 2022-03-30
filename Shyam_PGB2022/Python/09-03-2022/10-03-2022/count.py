s = input()
al = di = sc = 0
for i in range(len(s)):
    if s[i].isalpha():
        al = al+1
    elif s[i].isdigit():
        di = di+1
    else:
        sc = sc+1
print(al)
print(di)
print(sc)
