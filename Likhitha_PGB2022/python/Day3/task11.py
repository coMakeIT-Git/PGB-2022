
#an “abstract” class, Box, and use it to define some methods which any box object should have: 
	#a. add, for adding any number of items to the box, 
	#b. empty, for taking all the items out of the box and returning them as a list, and 
	#c. count, for counting the items which are currently in the box. 

class Box:
    def add(self, *items):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

#simple Item class which has a name attribute and a value attribute 
# you can assume that all the items you will use will be Item objects

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *items):
        self._items.extend(items)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i.name, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)