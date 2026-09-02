# 3875. Construct Uniform Parity Array I
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        even_count = 0
        odd_count = 0
        for num in nums1 :
            is_even = num % 2
            if is_even :
                even_count += 1
            else :
                odd_count += 1

        return even_count == n or odd_count == n or (even_count > 0 and odd_count > 0)
