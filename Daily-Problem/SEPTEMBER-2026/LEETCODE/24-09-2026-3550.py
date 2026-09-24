# 3550. Smallest Index With Digit Sum Equal to Index
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n) :
            digit_sum = 0
            num = nums[i]
            while num :
                digit_sum += num % 10
                num //= 10
            
            if digit_sum == i :
                return i
                
        return -1
