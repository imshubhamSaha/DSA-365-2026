# Max sum in the configuration
 
class Solution:
    def maxSum(self, arr):
        n = len(arr)
        curr = 0
        total = 0

        for i in range(n) :
            curr += arr[i] * i 
            total += arr[i]
        
        maximum = curr

        for i in range (n-1):
            curr = curr + total - n * arr[n - 1 - i]
            maximum = max(curr, maximum)

        
        return maximum
