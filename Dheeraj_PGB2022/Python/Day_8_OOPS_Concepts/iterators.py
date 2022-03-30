# 7. Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations


class itr:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


iterator = itr()
myiterator = iter(iterator)

for i in range(19):
    print(next(myiterator), end=",")

print(next(myiterator))
