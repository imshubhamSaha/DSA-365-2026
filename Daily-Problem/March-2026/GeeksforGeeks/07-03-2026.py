# Dice throw



class Solution:
    def noOfWays(self, m,n,x):
        dp = [[0]*(n+1) for _ in range(x+1)]
        dp[0][0] = 1
        for s in range(1, x+1):
            for i in range(1, n+1):
                for k in range(1, m+1):
                    if s-k >= 0:
                        dp[s][i] += dp[s-k][i-1]
        
        return dp[-1][-1]