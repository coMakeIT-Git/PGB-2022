import string

s = input()
new = s.translate(str.maketrans('', '', string.punctuation))
print(new)

