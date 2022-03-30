n=int(input("enter the number of rows:"))
for i in range(0, n):
    for j in range(n-i,0,-1):
        print(j, end=' ')
    print("")

str=input("please enter the string")
n=len(str)
alpha=digit=special=0
for i in range(n):
    if(str[i].isalpha()):
        alpha+=1
    elif(str[i].isdigit()):
        digit+=1
    else:
        special+=1
print("alphabets are:",alpha)
print("digits are:",digit)
print("special character are:",special)

s = "sreeja"
t = "kotagiri"
s_len = len(s)
t_len = len(t)


length = s_len if s_len > t_len else t_len
u = ""
t = t[::-1]

# iterate string 
for i in range(length):
    if i < s_len:
        u = u + s[i]
    if i < t_len:
        u = u+ t[i]

print("new string is: " +u)





