#Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(list_of_dicts(marks))
print("#########")

#Write a Python program to convert a given list of tuples to a list of strings using map function.
def combine(n):
    res = list(map(' '.join,n))
    return res
s = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(combine(s))
print("##########")

#Write a generator function which takes an integer n as a parameter.
    # The function should return a generator which counts down from n to 0.
    # Test your function using a for loop.

def count_down(limit):
    n=limit
    while n>0:
        yield n
        n=n-1
x=count_down(10)
for i in x:
    print(i)












