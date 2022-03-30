a = ('k1', 'k2', 'k3')
b = '5'
d = dict.fromkeys(a, b)
print(d)
dicti = {"FirstName": "Shyam", "MiddleName": "sai", "LastName": "Dogga", "Age": 21}
print(dicti)
print(dicti["FirstName"])
del dicti['MiddleName']
print(dicti)
dicti.popitem()
print(dicti)

