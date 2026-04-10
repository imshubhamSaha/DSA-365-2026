#Count increasing Subarrays

class Solution:
    def countIncreasing(self, arr):
        n = len(arr)
        valid_subarray_count = 0
        left = 0
        right = 1
        
        while right < n :
            if arr[right] <= arr[right - 1] :
                left = right
                
            valid_subarray_count += (right - left)
            right += 1
            
        return valid_subarray_count
