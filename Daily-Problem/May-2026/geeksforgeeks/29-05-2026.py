#Count Sorted Digit Groupings


class Solution:
    def validGroups(self, s):
        n = len(s)

        # dp[index][prev_sum]
        dp = [[-1] * 901 for _ in range(n + 1)]

        def solve(index, prev_sum):
            # If entire string is processed
            if index == n:
                return 1

            # Memoization check
            if dp[index][prev_sum] != -1:
                return dp[index][prev_sum]

            ans = 0
            curr_sum = 0

            # Generate all possible substrings
            for i in range(index, n):
                curr_sum += int(s[i])

                # Non-decreasing condition
                if curr_sum >= prev_sum:
                    ans += solve(i + 1, curr_sum)

            dp[index][prev_sum] = ans
            return ans

        return solve(0, 0)


        
