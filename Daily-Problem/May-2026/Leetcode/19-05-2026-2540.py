# 2540. Minimum Common Value
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        l1 = 0
        l2 = 0

        while l1 < n and l2 < m :
            if nums1[l1] == nums2[l2] :
                return nums1[l1] 
            elif nums1[l1] < nums2[l2] :
                l1 += 1
            else :
                l2 += 1

        return -1
