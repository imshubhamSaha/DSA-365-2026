# 2089. Find Target Indices After Sorting Array

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n = len(nums)
        if target > nums[-1] :
            return []
        
        left = 0
        indices = []
        while left < n and nums[left] != target :
            left += 1
        
        while left < n and nums[left] == target :
            indices.append(left)
            left += 1
        
        return indices
