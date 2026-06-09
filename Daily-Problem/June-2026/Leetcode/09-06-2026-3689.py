# 3689. Maximum Total Subarray Value I
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxi = nums[0]
        mini = nums[0]

        for num in nums :
            maxi = max(maxi, num)
            mini = min(mini, num)

        return (maxi - mini) * k
