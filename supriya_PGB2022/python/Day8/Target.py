#Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
#Note: Do not use the same element twice.
#Input: numbers= [10,20,10,40,50,60,70], target=50
#Output: 3, 4
class Target:
  def sum(self, arr, t):
       d = {}
       for i, n in enumerate(arr):
           if t - n in d:
               return (d[t - n], i )
           d[n] = i
print("index1=%d, index2=%d" % Target().sum((10,30,10,20,50,60),20))
  

    