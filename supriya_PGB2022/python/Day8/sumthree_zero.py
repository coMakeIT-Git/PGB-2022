#Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
#Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
#Output : [[-10, 2, 8], [-7, -3, 10]]
class sumthree_zero:
    def threeSum(self, arr):
      n=len(arr)
      res=[]   
      for i in range(0, n-2): 
        for j in range(i+1, n-1): 
          for k in range(j+1, n): 
              if (arr[i] + arr[j] + arr[k] == 0): 
                    res.append([arr[i], arr[j], arr[k]]) 
      return res            
print(sumthree_zero().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))        
