s = "Sriman25 is Data scientist50 and AI Expert"
out = []
temp = s.split()
for i in temp:
    if any(j.isalpha() for j in i) and any(j.isdigit() for j in i):
        out.append(i)
print(str(out))