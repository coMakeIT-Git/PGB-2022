s = input()
out = []
temp = s.split()
for i in temp:
    if any(j.isalpha() for j in i) and any(j.isdigit() for j in i):
        out.append(i)
print(str(out))