# Write an “abstract” class, Box, and use it to define some methods
from abc import ABC, abstractmethod
# Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects.
class Item:
    def __init__(self,name,value):
        self.name=name
        self.value=value

class Box(ABC):
    #empty, for taking all the items out of the box and returning them as a list
    @abstractmethod
    def empty(self):
        pass

    #count, for counting the items which are currently in the box.
    @abstractmethod
    def count(self):
        pass

    #add, for adding any number of items to the box,
    @abstractmethod
    def add(self, *items):
        pass

#write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.
class ListBox(Box):
    def __init__(self):
        self._items = []

    def empty(self):
        items = self._items
        self._items = []
        return items

    def displayItems(self):
        if self.count() == 0:
            print("Not Found any items")
            return
        print("Item Attributes: ")
        for i in self._items:
            print("Name:{}, Value:{}".format(i.name,i.value))
        return

    def count(self):
        return len(self._items)

    def add(self, *items):
        self._items.extend(items)


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def displayItems(self):
        if self.count() == 0:
            print("Not Found any items")
            return
        print("Item Attributes: ")
        for k, v in self._items.items():
            print("Name:{}, Value:{}".format(k,v))
        return

    def count(self):
        return len(self._items)

    def add(self, *items):
        self._items.update(dict((i.name, i.value) for i in items))


item1 = Item("fruits", 1)
item2 = Item("vegetables", 2)
item3 = Item("books", 3)
item4 = Item("cars", 4)
item5 = Item("colors", 5)
print("List Box:")
ListBox_obj = ListBox()
ListBox_obj.add(item1, item2, item3)
ListBox_obj.displayItems()
ListBox_obj.empty()
ListBox_obj.displayItems()
print("\nDictionary Box:")
DictBox_obj = DictBox()
DictBox_obj.add(item4, item5)
DictBox_obj.displayItems()
DictBox_obj.empty()
DictBox_obj.displayItems()









