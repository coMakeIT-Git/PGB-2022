s = "I am 20 years and and 22 months old"
n = filter(str.isdigit, s)
k = "".join(n)
print("\n Digits in the string are:", k)