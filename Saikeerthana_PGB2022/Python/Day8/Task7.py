"""Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations"""
class Numbers:
  def __iter__(self):
    self.x = 1
    return self

  def __next__(self):
    if self.x <= 20:
      res = self.x
      self.x += 1
      return res
    else:
      raise StopIteration

myclass = Numbers()
myiter = iter(myclass)

for i in myiter:
  print(i)