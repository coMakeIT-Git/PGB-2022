class Box:
    def add(self, *i):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ListBox(Box):
    def __init__(self):
        self.i1 = []

    def add(self, *i):
        self.i1.extend(i)

    def empty(self):
        i = self.i1
        self.i1 = []
        return i

    def count(self):
        return len(self.i1)


class DictBox(Box):
    def __init__(self):
        self.d1 = {}

    def add(self, *i):
        self.d1.update(dict((j.name, j) for j in i))

    def empty(self):
        d = list(self.d1.values())
        self.d1 = {}
        return d

    def count(self):
        return len(self.d1)

