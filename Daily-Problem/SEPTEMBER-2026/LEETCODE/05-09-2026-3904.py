# 3904. Smallest Stable Index II

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_smallest = [0] * n
        suffix_smallest[n - 1] = nums[n-1]

        for i in range(n-2, -1, -1) :
            suffix_smallest[i] = min(nums[i], suffix_smallest[i+1])

        prefix_largest = -1

        for i in range(n) :
            prefix_largest = max(prefix_largest, nums[i])
            instability_score = prefix_largest - suffix_smallest[i]
            if instability_score <= k :
                return i
                
        return -1
