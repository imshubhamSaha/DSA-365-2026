# 1848. Minimum Distance to the Target Element


class Solution:
    def getMinDistance(self, nums, target, start):
        left = 0
        right = len(nums) - 1
        if nums[start] == target:
            return 0
        min_dist = right + 1

        while left <= right:
            if nums[left] == target:
                min_dist = min(min_dist, abs(start - left))
            if nums[right] == target:
                min_dist = min(min_dist, abs(start - right))
            left += 1
            right -= 1

        return min_dist
