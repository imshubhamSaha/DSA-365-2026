# Minimum Moves to Sort Permutation
class Solution:
    def minMoves(self, arr):
        n = len(arr)
        dp = {}
        max_len = 0

        for num in arr:
            dp[num] = dp.get(num - 1, 0) + 1
            max_len = max(max_len, dp[num])

        return n - max_len
