# Check Subset sum divisible by k

class Solution:
    def divisibleByK(self, arr, k):
        # code here
        dp = [[False] * k for _ in range(len(arr) + 1)]
        dp[0][0] = True
        for i, v in enumerate(arr):
            for j in range(k):
                if dp[i][j]:
                    dp[i+1][j] = True
                    rem = (j + v) % k
                    if rem == 0:
                        return True
                    dp[i+1][rem] = True
        return False
      
