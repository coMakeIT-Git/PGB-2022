""" Write a Python class to find the three elements that sum to zero from a set of n real numbers.
	Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
	Output : [[-10, 2, 8], [-7, -3, 10]]"""

class triplesum:
    def findTriplets(arr, n):
        found=False
        arr.sort()
        for i in range(0, n - 1):
            l=i+1
            r=n-1
            x=arr[i]
            while (l<r):
                if(x+arr[l]+arr[r]==0):
                    print([x,arr[l],arr[r]])
                    l+=1
                    r-=1
                    found=True
                elif ( x+arr[l]+arr[r]<0 ):
                    l+=1
                else:
                    r-=1
        if(found==False):
            print("No Triplet found")

arr = [0, -1, 2, -3, 1]
n = len(arr)

print("Triplets Whose sum is equal to zero:")
triplesum.findTriplets(arr, n)



