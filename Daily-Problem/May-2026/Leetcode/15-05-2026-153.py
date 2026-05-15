# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return nums[0]
        left = 0
        right = n - 1
        if nums[0] < nums[n-1] :
            return nums[0]

        while left < right :
            mid = left + (right - left) // 2

            if nums[mid] >= nums[left] and nums[mid] > nums[right] :
                left = mid + 1
            else :
                right= mid
           
        
        return nums[right]
