#Partitions with Given Difference

class Solution:
    def solve(self,arr, i, d, dp, bais, left):
        if(i == len(arr)):
            return 1 if d == 0 else 0
        
        if left < d :
            return 0
            
        if dp[i][d+ bais] != -1 :
            return dp[i][d+bais]
            
        dp[i][d+ bais] = (self.solve(arr, i+1, d+ arr[i], dp, bais, left - arr[i]) +
                        self.solve(arr, i+1, d - arr[i], dp, bais, left - arr[i]))%1000000007;
        
        return dp[i][d+bais]
    
    
    def countPartitions(self, arr, diff):
        n = len(arr)
        total_sum = sum(arr)
        
        
            
        dp = [[-1] * (2 * total_sum + 1) for _ in range(n)]
        return self.solve(arr, 0, diff , dp, total_sum - diff , total_sum)
        
