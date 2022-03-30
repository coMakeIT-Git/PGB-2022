elements =['a', 'b', 'c']
di ='10'
x=dict.fromkeys(elements,di)
print(x)

details= {"sreeja":21,"sai":22,"vaishu":23} 
print("Dict is",details)	
print("value of sai:",details.get("sai"))
print("Keyvalue pairs are:",details)
result=details.pop("vaishu")
print("Dictionary after removing element", details)
result=details.popitem()
print("Dictionary after removing last keyvalue pair",details)

print("creating a set")
fruits = {"apple", "banana", "cherry","mango","pineaple"} 
print("Set is",fruits)	
fruits.add("kiwi")
print("after adding kiwi",fruits)
fruits.remove("banana")
print("after removing banana",fruits)

x={"sai","sreeja","vaishu","aishu","vani","yuvaan"}
y={"sai","sreeja","karthikeya","aishu","sweety","lakshmi","vaishu"}
print("returning the set that doesnt contain elements present in set y",x.difference(y))
print("Removing the items that exist in both sets",x^y)
print("Return True if no items in set x is present in set y",x.isdisjoint(y))
print("Return True if all items in set x are present in set y",y.issuperset(x))
print("Return True if all items set y are present in set x",x.issuperset(y))
#Return a set that contains all items from both sets, except items that are present in both sets
print("Removing the items ",x^y)
z = x.intersection(y)
print(z)
x.update(y)
print("Inserting the items from set y into set x",x)



