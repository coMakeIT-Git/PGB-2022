from abc import ABC,abstractmethod
class Box(ABC):
	@abstractmethod
	def add(this):pass
	@abstractmethod
	def empty(this):pass
	@abstractmethod
	def count(this):pass
class Item:
	def __init__(self,name,value):
		self.name=name
		self.value=value
class ListBox(Box):
	list=[]
	def add(this,*items):
		this.list.extend(items)
	def empty(this):
		this.ans=this.list.copy()
		this.list.clear()
		for i in this.ans:
			print(i.name)
		return this.ans
	def count(this):
		return len(this.list)
class DictBox(Box):
	d={}
	def add(this,*items):
		for i in items:
			this.d[i.name]=i.value
	def empty(this):
		this.ans=this.d.copy()
		d=dict()
		return this.ans
	def count(this):
		return len(this.d)

l=ListBox()
e=Item("adithya",5)
f=Item("akhil",10)
g=Item("balaji",15)
l.add(e,f,g)
d=DictBox()
d.add(e,f,g)
abc=d.empty()
for key,item in abc.items():
	print(key,item)
ans=l.empty()
for i in ans:
	print(i.name,i.value)
