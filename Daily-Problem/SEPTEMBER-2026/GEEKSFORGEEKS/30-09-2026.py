#Ways to Reach Origin
class Solution:
    def ways(self, x: int, y: int) -> int:
        mod = (10 ** 9) + 7
        dp = [[0] * (x + 1) for _ in range(y + 1)]
        for i in range(y + 1):
            for j in range(x + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
        return dp[y][x]
