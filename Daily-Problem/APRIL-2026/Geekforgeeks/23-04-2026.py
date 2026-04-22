#Two Equal Sum Subarrays
class Solution:
    def canSplit(self, arr):
        n = len(arr)
        prefix_sum = sum(arr)
        if prefix_sum % 2 :
            return False
        
        suffix_sum = 0
        
        for i in range(n - 1, 0,-1) :
            suffix_sum += arr[i]
            prefix_sum -= arr[i]
            if suffix_sum == prefix_sum :
                return True
            if suffix_sum > prefix_sum :
                return False
                
        return prefix_sum == suffix_sum
