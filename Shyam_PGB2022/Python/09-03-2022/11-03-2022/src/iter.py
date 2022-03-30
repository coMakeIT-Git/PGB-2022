class Iter:
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= 20:
            x = self.n
            self.n += 1
            return x
        else:
            raise StopIteration


object = Iter()
process = iter(object)

for x in process:
    print(x)
