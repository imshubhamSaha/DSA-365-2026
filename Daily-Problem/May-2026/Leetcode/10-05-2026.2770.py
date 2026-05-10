# 2770. Maximum Number of Jumps to Reach the Last Index
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        memo = {}

        def dfs(i):
            if i == n - 1:
                return 0

            if i in memo:
                return memo[i]

            max_jumps = -float('inf')

            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    res = dfs(j)

                    if res != -float('inf'):
                        max_jumps = max(max_jumps, 1 + res)

            memo[i] = max_jumps
            return memo[i]

        ans = dfs(0)

        return ans if ans != -float('inf') else -1
