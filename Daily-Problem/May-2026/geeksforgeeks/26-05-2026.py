# Minimum Toggle to Partition

class Solution:
    def minToggle(self, arr):
        n = len(arr)
        toggle = n
        right_ones = sum(arr)
        left_ones = 0
        
        for i in range(-1,n) :
            if i >= 0 :
                left_ones += arr[i]
                right_ones -= arr[i]
            
            left_cost = left_ones 
            right_cost = (n - i - 1) - right_ones
            
            toggle = min(toggle, (left_cost + right_cost))
            
        return toggle
