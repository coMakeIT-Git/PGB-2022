#Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples:
#[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#Sorting the List of Tuples:
#[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
tuple=[('Delhi',2400),('Kerala',300),('Lucknow',2000),('Maharastra',1100)]
print("Original tuple is:",tuple)
tuple.sort(key = lambda x: x[1])
print("After sorting using lambda:",tuple)

#Write a Python program to sort a list of dictionaries by color using Lambda.
#Original list of dictionaries :[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#Sorting the List of dictionaries :[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, 
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
dict = [{'shape':'Circle', 'color':'Black'}, {'shape':'Triangle', 'color':'Purple'}, {'shape':'Square', 'color':'Orange'}]
print("Original dict is :",dict)
dict.sort(key = lambda x: x['color'])
print("\nAfter sorting using lambda :",dict)

