# Min Product Subset
class Solution:
    def minProd(self, arr):
        n = len(arr)
        negCount = 0
        zeroCount = 0
        maxNeg = float('-inf')
        minPos = float('inf')
        prod = 1

        for x in arr:
            if x == 0:
                zeroCount += 1
                continue

            if x < 0:
                negCount += 1
                maxNeg = max(maxNeg, x)

            if x > 0:
                minPos = min(minPos, x)
            prod *= x
        if zeroCount == n:
            return 0
        if negCount == 0:
            if zeroCount > 0:
                return 0
            return minPos
        if negCount % 2 == 1:
            return prod
        prod //= maxNeg
        return prod
