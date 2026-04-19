# 1855. Maximum Distance Between a Pair of Values
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        left = 0
        right = 1

        while left < n and right < m :
            left += nums1[left] > nums2[right]
            right += 1

        return right - left - 1
