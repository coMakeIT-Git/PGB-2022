
#Python program to sort a list of dictionaries by color using Lambda

import keyword


dict=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print("Original dictionary ", dict)

print("After sorting using lambda exp by color : ")

dict.sort(key= lambda x:x['color'])
print(dict)
