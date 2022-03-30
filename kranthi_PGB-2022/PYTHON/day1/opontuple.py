t=10,20,30,40,50,10,60,10
print(t)
print("Occurrence of a specified value=10 in the tuple:")
print(t.count(10))
res = None
r=int(input("Enter number to find position"))
for i in range(0,len(t)):
    if(t[i]==r):
        res=i+1
        break
if (res==None):
    print("no such Number exixts exists")
else:
    print("the Number {} is present at position {}".format(r,res))



