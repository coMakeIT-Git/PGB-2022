from unittest import result


class threesum:
    def sum(self,numarr):
        numarr, result, i = sorted(numarr), [], 0
        while i < len(numarr) - 2:
            j, k = i + 1, len(numarr) - 1
            while j < k:
                if numarr[i] + numarr[j] + numarr[k] < 0:
                    j += 1
                elif numarr[i] + numarr[j] + numarr[k] > 0:
                    k -= 1
                else:
                    result.append([numarr[i], numarr[j], numarr[k]])
                    j, k = j + 1, k - 1
                    while j < k and numarr[j] == numarr[j - 1]:
                        j += 1
                    while j < k and numarr[k] == numarr[k + 1]:
                        k -= 1
            i += 1
            while i < len(numarr) - 2 and numarr[i] == numarr[i - 1]:
                i += 1
        return result


print(threesum().sum([-25, -10, -7, -3, 2, 4, 8, 10]))

