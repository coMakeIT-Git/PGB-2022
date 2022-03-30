#Write a Python program to sort a list of tuples using Lambda.
a=[('English', 88), ('Science', 90), ('Maths', 97), ('Social', 82)]
a.sort(key=lambda x:x[1])
print(a)
print("########")

#Write a Python program to sort a list of dictionaries by color using Lambda.
dict=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
dict.sort(key=lambda x:x["color"])
print(dict)
print("#####")






