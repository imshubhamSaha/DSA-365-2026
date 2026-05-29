# 3300. Minimum Element After Replacement With Digit Sum
class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini_element = 100000

        for num in nums :
            curr = num 
            curr_sum = 0
            while curr :
                curr_sum += curr % 10
                curr = curr // 10

            mini_element = min(mini_element, curr_sum)

        return mini_element
