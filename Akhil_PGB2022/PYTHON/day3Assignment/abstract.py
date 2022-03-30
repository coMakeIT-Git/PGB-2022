from abc import ABC, abstractmethod
 
class Box(ABC):
	@abstractmethod
	def add(self,*items):
		pass
	@abstractmethod
	def empty(self):
		pass
	@abstractmethod
	def count(self):
		pass
	
class item():
	def __init__(this,name,val):
		this.name = name
		this.value =val

class Listbox(Box):
	def __init__(self):
		self.lst = []
	
	def empty(self):
		z = self.lst
		self.lst = []
		return z
	
	def displayItems(self):
		if self.count() == 0:
			print("No Items Found")
			return
		print("Item Attributes in list: ")
		for i in self.lst:
			print("Name :",i.name, "Value :",i.value)
		return

	def count(self):
		return len(self.lst)

	def add(self, *items):
		self.lst.extend(items)
	

class Dictbox(Box):
	def __init__(self):
		self._items = {}

	def empty(self):
		items = list(self._items.values())
		self._items = {}
		return items

	def displayItems(self):
		if self.count() == 0:
			print("No Items Found")
			return
		print("Item Attributes in dict: ")
		for k, v in self._items.items():
			print(f"Name : {k}, Value : {v}")
		return

	def count(self):
		return len(self._items)

	def add(self, *items):
		self._items.update(dict((i.name, i.value) for i in items))
        
        
i1 = item("item1",1)   
i2 = item("item2",2)   
i3 = item("item3",3)        
l = Listbox()
l.add(i1,i2,i3)
l.displayItems()
print(l.count())

d = Dictbox()
d.add(i1,i2,i3)
d.displayItems()
print(d.count())
