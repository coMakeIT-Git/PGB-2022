class Number:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num<=20:
            x=self.num
            self.num+=1
            return x
        else:
            raise StopIteration
numobj=Number()
numiter=iter(numobj)
for i in numiter:
    print(i)


