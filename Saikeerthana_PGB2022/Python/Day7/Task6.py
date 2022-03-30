#Find the largest item from a given list without using inbuilt methods
list=["1","5","4","7","2"]
max=list[0]
for i in list:
    if(i>max):
        max=i
print("largest number is:",max)