class triplets:
    def tripletcost(arr, n):
        flag = False
        for i in range(0, n - 2):

            for j in range(i + 1, n - 1):

                for k in range(j + 1, n):

                    if (arr[i] + arr[j] + arr[k] == 0):
                        print("[",arr[i], arr[j], arr[k],"]")
                        flag = True
        if (flag == False):
            print(" NULL ")

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
triplets.tripletcost(arr, n)

