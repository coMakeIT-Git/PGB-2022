#TASK-3

#lists are mutable
colorList = ["Red", "Yellow", "Green"]
colorList.insert(2, "Black")
print(colorList) #prints ["Red","Black","yellow","Green"]

#Dictionaries are mutable
student = {"name": "Sam","Father Name": "John"}
student["Father name"]="satyam naidu"
print(student)#prints {'name': 'Sam','Father name': 'satyam naidu'}

#sets are mutable
set2 = {1, "python", "android", "java"}
set2.add("ruby")
print(set2)#prints  {‘android’, ‘java’, ‘ruby’, ‘python’}

#string is immutable
string = "Welcome to EyeHunts"
#string[0] = 'Hello'
print(type(string)) #TypeError:'str' does not support item assignment

#tuples are immutable
t = ('a', 'b', 'c', 'd', 'e')
#t[0] = 'A'
print(type(t)) #TypeError: object doesn't support item assignment