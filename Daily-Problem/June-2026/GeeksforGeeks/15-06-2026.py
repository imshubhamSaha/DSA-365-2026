# Minimum Cost to Fill Given Weight

class Solution:
    def minimumCost(self, cost, w):
        n = len(cost)
        INF = 10**9
        dp = [INF] * (w + 1)
        
        dp[0] = 0
        for i in range(n) :
            if cost[i] == -1:
                continue

            wt = i + 1

            for j in range(wt, w + 1):
                if dp[j - wt] != INF:
                    dp[j] = min(dp[j], cost[i] + dp[j - wt])

        return dp[w] if dp[w] != INF else -1
        
