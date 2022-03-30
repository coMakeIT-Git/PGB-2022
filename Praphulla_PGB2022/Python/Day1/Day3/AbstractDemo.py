from abc import ABC, abstractmethod


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Box(ABC):
    def __init__(self, items):
        self.items = items

    @abstractmethod
    def add(self, add_items):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def count(self):
        pass


class ListBox(Box):
    def __init__(self, items=None):
        if items is None:
            items = []
        super(ListBox, self).__init__(items)

    def add(self, *add_items):
        self.items.extend(add_items)

    def empty(self):
        items = self.items.copy()
        self.items.clear()
        return items

    def count(self):
        return len(self.items)


class DictBox(Box):
    def __init__(self, items=None):
        if items is None:
            items = {}
        super(DictBox, self).__init__(items)

    def add(self, *add_items):
        for add_item in add_items:
            self.items[add_item.name] = add_item.value

    def empty(self):
        items = self.items.copy()
        self.items.clear()
        return items

    def count(self):
        return len(self.items)