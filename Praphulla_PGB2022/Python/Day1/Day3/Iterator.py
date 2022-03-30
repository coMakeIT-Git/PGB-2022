class Iterator:
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
i = Iterator()
process = iter(i)
print("\n Printing the values of till 20:")
for x in process:
    print("\t", x)