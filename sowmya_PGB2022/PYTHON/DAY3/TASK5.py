class Pair:
    def func(a,k):
        map1={}
        for i,num in enumerate(a):
            if(k-num in map1):
                print("Pair of indices are : {}, {}".format(map1[k-num]+1,i+1))
            map1[num]=i
n=int(input("Enter array size : "))
a=[]
for i in range(n):
    b=int(input(""))
    a.append(b)
k=int(input("Enter value to be searched: "))
Pair.func(a,k)