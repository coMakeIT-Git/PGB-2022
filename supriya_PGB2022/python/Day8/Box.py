#Write an “abstract” class, Box, and use it to define some methods which any box object should have: 
#a.add, for adding any number of items to the box, 
#b.empty, for taking all the items out of the box and returning them as a list, and 
#c.count, for counting the items which are currently in the box. 
#d.Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects. 
#e.Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.
class Box:
    def add(self, *books):
        raise NotImplementedError()
    def empty(self):
        raise NotImplementedError()
    def count(self):
        raise NotImplementedError()
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class ListBox(Box):
    def __init__(self):
        self._books = []
    def add(self, *books):
        self._books.extend(books)
    def empty(self):
        books = self._books
        self._books = []
        return books
    def count(self):
        return len(self._books)
class DictBox(Box):
    def __init__(self):
        self._books = {}
    def add(self, *books):
        self._books.update(dict((i.name, i) for i in books))
    def empty(self):
        books = list(self._books.values())
        self._books = {}
        return books
    def count(self):
        return len(self._books)