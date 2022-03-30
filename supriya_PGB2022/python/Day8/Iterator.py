#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations
class Iterator:
  def __iter__(self):
    self.i = 1
    return self

  def __next__(self):
    if self.i <= 20:
      x = self.i
      self.i += 1
      return x
    else:
      raise StopIteration

mycls = Iterator()
myiter = iter(mycls)

for x in myiter:
  print(x)