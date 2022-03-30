#Python class to find a pair of elements (indices of the two numbers) 
# from a given array whose sum equals a specific target number.

class Pair:
    def func(a,k):
        map1={}
        for i,num in enumerate(a):
            if(k-num in map1):
                print("Pair of indices are : {}, {}".format(map1[k-num],i))
            map1[num]=i
                
    
    

n=int(input("Enter array size : "))
a=[]

for i in range(n):
    b=int(input("Enter value: "))
    a.append(b)
    
k=int(input("Enter value to be searched: "))

print("Pair of indices: ")
Pair.func(a,k)