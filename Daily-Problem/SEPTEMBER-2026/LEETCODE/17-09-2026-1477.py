# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        result, total, i = n + 1, 0, 0
        dp = [n] * (n + 1)

        for j in range(n):
            total += arr[j]

            while total > target:
                total -= arr[i]
                i += 1
            
            dp[j + 1] = dp[j]

            if total == target:
                Len = j - i + 1

                result = min(result, Len + dp[i])
                dp[j + 1] = min(dp[j], Len)
            
        return -1 if result == n + 1 else result
