from os import remove
import sunau


days=["mon","tue","wed","thu","fri","sat","sun"]
months=["jan","feb","mar","apr","may","june","july"]
day=[]
print("adding elements into list days")
days.append("sun")
print(days)
print("copying the days list into day list")
day=days.copy()
print(day)
print("return the number of sun in days list")
print(days.count("sun"))

print("adding elements of months list to days list")
list3=days+months
print(list3)
print("position of sun",list3.index("sun"))

print("inserting the value tue at position 2 in ")
days[2]="tue"
print(days)

print("removing the value at position 2  ")
days.pop(2)
print(days)

print("removing the sun from the list")
days.remove("sun")
print(days)

print("reversing the order of the days list")
days.reverse()
print(days)

print("sorting the list")
days.sort()
print(days)