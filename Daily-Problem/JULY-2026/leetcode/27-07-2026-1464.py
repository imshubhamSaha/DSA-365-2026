# 1464. Maximum Product of Two Elements in an Array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        largest = nums[0]
        second_largest = -1

        for i in range(1, n) :
            if nums[i] >= largest :
                second_largest = largest
                largest = nums[i]
            elif nums[i] > second_largest :
                second_largest = nums[i]

        return (largest - 1) * (second_largest - 1)
