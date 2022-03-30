fruits = ['apple', 'banana', 'cherry']
fruits1=fruits.copy() #to copy one list in to the other

cars=['Ford','BMW','volvo']
fruits.append('mango')
print(fruits)
fruits.clear()
print("list after removing all elemnts using clear")
print(fruits)

print(fruits1)
print("Occurrence of cherry in fruits list = ",fruits1.count('cherry'))
print("\n")


fruits1.extend(cars)
print("list extending list using l1.extend(l2)")
print(fruits1)
print("Index of cherry : ",fruits1.index('cherry'))
fruits1.insert(2,'orange')
print("List after inserting orange at 2",fruits1)
fruits1.pop(2)
fruits1.remove('banana')
fruits1.reverse()
print("list after removing element at 2 and banana ,reversing the list")
print(fruits1)
cars.sort()
print("cars list after sorting",cars)
print("\n")


