#1846. Maximum Element After Decreasing and Rearranging

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        integer_used = 1
        
        for i in range(1, n) :
            integer_used = min(arr[i] , integer_used + 1)
        
        return integer_used


            
