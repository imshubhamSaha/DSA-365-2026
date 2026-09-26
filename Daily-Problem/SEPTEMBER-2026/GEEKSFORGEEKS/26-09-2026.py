# Minimum Cost Pizza Selection

class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        # code here
        dp = [float('inf')]*(x+1)
        dp[0] = 0
        for e in range(1, x+1):
            dp[e] = min(dp[e], dp[max(e-s, 0)]+cs)
            dp[e] = min(dp[e], dp[max(e-m, 0)]+cm)
            dp[e] = min(dp[e], dp[max(e-l, 0)]+cl)
        return dp[-1]
