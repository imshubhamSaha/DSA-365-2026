# 3010. Divide an Array Into Subarrays With Minimum Cost I

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        
        second_lowest = 52
        third_lowest = 53

        for i in range(1,n) :
            if nums[i] <= second_lowest :
                third_lowest = second_lowest
                second_lowest = nums[i]
            elif nums[i] <= third_lowest :
                third_lowest = nums[i]

        return nums[0] + second_lowest + third_lowest