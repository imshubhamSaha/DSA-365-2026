# Missing Element in Range


class Solution:
    def missingRange(self, arr, low, high):
        s = set(arr)
        
        reult = []
        
        for num in range(low, high + 1):
            if num not in s:
                reult.append(num)
            
        return reult
