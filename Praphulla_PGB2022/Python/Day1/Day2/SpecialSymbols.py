import string
s = input()
x = s.translate(str.maketrans('', '', string.punctuation))
print(str(x))
