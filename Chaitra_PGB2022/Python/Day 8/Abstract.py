from abc import ABC

class Box(ABC):
    def add(self, item):
        pass
    def empty(self):
        pass
    def count(self):
        pass

class Item():
    def __init__(self, Name, Value):
        self.Name = Name
        self.Value = Value

class ListBox(Box, list):
    def __init__(self):
        self = list()

    def add(self, item):
        lst = [item.Name, item.Value]
        self.append(lst)

    def empty(self):
        self.clear()

    def count(self):
        return len(self)


class DictBox(Box, dict):
    def __init__(self):
        self = dict()

    def add(self, item):
        self[item.Name] = item.Value

    def empty(self):
        self.clear()

    def count(self):
        return len(self)

i1 = Item("Red", 1)
i2 = Item("Blue", 2)
i3 = Item("Black", 3)
i4 = Item("Yellow", 4)
i5 = Item("Triangle", "Cyan")
i6 = Item("Square", "Magenta")

l = ListBox()
l.add(i1)
l.add(i2)
l.add(i3)
l.add(i4)
print("Items in ListBox: ", l)
print("Count: ", l.count())


d = DictBox()
d.add(i5)
d.add(i6)
print("\nItems in DictBox: ", d)
print("Count: ", d.count())

print("\nEmptying DictBox...")
d.clear()
print(d)

