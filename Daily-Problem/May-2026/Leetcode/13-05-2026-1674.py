# 1674. Minimum Moves to Make Array Complementary
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):

            a = nums[i]
            b = nums[n - i - 1]

            if a > b:
                a, b = b, a

            summ = a + b

            left = a + 1
            right = b + limit

 
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            diff[left] -= 1
            diff[right + 1] += 1
            diff[summ] -= 1
            diff[summ + 1] += 1

        res = float('inf')
        curr = 0

        for s in range(2, 2 * limit + 1):
            curr += diff[s]
            res = min(res, curr)

        return res
