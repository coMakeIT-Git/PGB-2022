class NotValidAge(Exception):
  """Raised when the age is less than 18"""
  def __str__(self):
    return "Age should be greater than 18 years."
def validity(age):
  if age < 18:
    raise NotValidAge
try:
    validity(16)

except NotValidAge:
    print("not valid")

li=[1,2,3]
try:
    print(li[3])
except IndexError as ex:
    print("Error message",ex)
try:
    print(1/0)
except ZeroDivisionError as ex:
    print("Error message",ex)
try:
    from re import notexisting
except ImportError as ex:
    print("Error message",ex)
try:
    x='abc'
    res=int(x)
except ValueError as ex:
    print("Error message",ex)
try:
    for i in range(0,5):
        print(i)
except IndentationError as ex:
    print("Error message",ex)
else:
    print("Not executed")
finally:
    print('finally block executes always ') 


