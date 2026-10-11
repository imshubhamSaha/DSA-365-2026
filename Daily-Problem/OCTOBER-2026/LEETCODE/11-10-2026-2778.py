# 2778. Sum of Squares of Special Elements 

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        square_sum = 0

        for i in range(n) :
            if (n % (i + 1)) == 0 :
                square_sum += nums[i] * nums[i]

        return square_sum
