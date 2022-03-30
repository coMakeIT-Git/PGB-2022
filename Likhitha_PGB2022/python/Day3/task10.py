
#Python program to split a given dictionary of lists into list of dictionaries using map function

dict1 ={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

print("Original dictionary: ",dict1)

print("After splitting the dictionary : ")

res = [dict(zip(dict1,i)) for i in zip(*dict1.values())]

print(res)

#Python program to convert a given list of tuples to a list of strings using map function.

list1=[('red', 'pink'), ('white', 'black'), ('orange', 'green')]

print("Original list Of tuples : ",list1)

print("After splitting: ")

res1=[''.join(i) for i in list1]

print(res1)


#generator function which takes an integer n as a parameter. 
# The function should return a generator which counts down from n to 0. Test your function using a for loop

def function(n):
    for x in range(n,-1,-1):
       if (x>=0): 
           yield x       
num = function(9)
print(list(num))