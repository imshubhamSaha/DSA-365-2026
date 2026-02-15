# Chocolate Distribution Problem



#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):
        n = len(arr)
        arr.sort()
        
        left = 0
        
        minimum_diff = 10000001
        
        while left <= (n - M) :
            minimum_diff = min(minimum_diff,(arr[left + M - 1] - arr[left]))
            left += 1
        
        return minimum_diff
