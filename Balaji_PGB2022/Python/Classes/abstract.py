from abc import ABC
class Box(ABC):
    def add():   pass
    def empty(): pass
    def count(): pass
class item(Box):
    def __init__(self,name,value):
        self.name=name
        self.value=value
class ListBox(Box):
    ans=[]
    def __init__(self):
        self.items=[]
    def add(self,*items):
        self.items.extend(items)
    def empty(self):
        self.ans=self.items.copy()
        self.items.clear()
        return self.ans
    def count(self):
        return len(self.ans)
class DictBox(Box):
    d={}
    def add(self,*items):
        for i in items:
            self.d[i.name]=i.value

    def empty(self):
        self.ans = self.d.copy()
        d = dict()
        return self.ans

    def count(self):
        return len(self.d)
lst=ListBox()
a=item("Balaji",10)
b=item("Akhil",20)
c=item("Aadithya",30)
lst.add(a,b,c)
ans=lst.empty()
for i in ans:
    print("Name is:",i.name,"Value is",i.value)
print("Count of list is:",lst.count())
dict1=DictBox()
dict1.add(a,b,c)
ans1=dict1.empty()
for key,items in ans1.items():
    print("Key is:",key, "Value is", items)







