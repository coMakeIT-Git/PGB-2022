# 17. Write an “abstract” class, Box, and use it to define some methods which any box object should have:
# 	a. add, for adding any number of items to the box,
# 	b. empty, for taking all the items out of the box and returning them as a list, and
# 	c. count, for counting the items which are currently in the box.
# 	d. Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects.
# 	e. Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.

class Box:
    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def add(self, *items):
        raise NotImplementedError()


class Item:
    def __init__(self, name, value):
        self.value = value
        self.name = name


class ListBox(Box):
    def __init__(self):
        self._items = []

    def empty(self):
        items = self._items
        self._items = []
        return items

    def displayItems(self):
        if self.count() == 0:
            print("No Items Found")
            return
        print("Item Attributes : ")
        for i in self._items:
            print(f"Name : {i.name}, Value : {i.value}")
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
            print("No Items Found")
            return
        print("Item Attributes : ")
        for k, v in self._items.items():
            print(f"Name : {k}, Value : {v}")
        return

    def count(self):
        return len(self._items)

    def add(self, *items):
        self._items.update(dict((i.name, i.value) for i in items))


i1 = Item("Red", 1)
i2 = Item("Blue", 2)
i3 = Item("Green", 3)
i4 = Item("Yellow", 4)
i5 = Item("Black", 5)
print("List Box\n")
ObjListBox = ListBox()
ObjListBox.add(i1, i2, i3)
ObjListBox.displayItems()
ObjListBox.empty()
ObjListBox.displayItems()
print("\n\nDictionary Box\n")
ObjDictBox = DictBox()
ObjDictBox.add(i4, i5)
ObjDictBox.displayItems()
ObjDictBox.empty()
ObjDictBox.displayItems()
