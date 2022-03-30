import math
class NotValidsalary(Exception):
  def __str__(self):
    return "salary should be greater than 15000."
def validity(salary):
  if salary < 15000:
    raise NotValidsalary
try:
    validity(10000)

except NotValidsalary:
    print("not valid salary")
try:
    a=10/0
    print(a)
except ZeroDivisionError:
    print("Zero Division Error occured")
else:
    print("valid division")

try:
    import abcd
except ImportError:
    print("cannot import  as import error is raised")
else:
    print("valid import")

try:
    a=[1,2,3,4,5]
    print(a[7])
except IndexError:
    print("index is out of range error raised")
else:
    print("no error ")

try:
    for i in range(5):
      print(i)

except:
    print(" error is raised")

else:
    print("There is no error")


try:
    import math
    print(math.sqrt(-1))

except ValueError:
    print("Invalid value and value error is raised")
else:
    print("valid value")

finally:
    print("These are different exceptions in python")
    