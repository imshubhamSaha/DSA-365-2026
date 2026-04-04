# Target Sum

class Solution:
    def totalWays(self, arr, target):
        n = len(arr)
        total=sum(arr)
        if (total+target)%2!=0 or abs(target)>total:
            return 0
        s=(target+total)//2
        
        dp=[[0 for _ in range(s+1)] for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(s+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return(dp[n][s])
