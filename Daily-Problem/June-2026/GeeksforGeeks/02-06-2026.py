#Pairs with certain difference


class Solution:
    def sumDiffPairs(self, arr, k):
        n = len(arr)
        arr.sort()
        pair_sum = 0
        i = n - 1
        while (i > 0) :
            if (arr[i] - arr[i-1]) < k :
                pair_sum += arr[i] + arr[i-1]
                i -= 2
                continue
            i -= 1
        
        return pair_sum
