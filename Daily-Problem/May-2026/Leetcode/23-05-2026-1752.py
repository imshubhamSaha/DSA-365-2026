#1752. Check if Array Is Sorted and Rotated
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotated = False
        for i in range(1,n) :
            if nums[i] < nums[i-1] and not rotated :
                rotated = True
            else :
                if nums[i] < nums[i-1] and rotated :
                    return False
        
        if rotated and nums[n-1] > nums[0] :
            return False
        return True
