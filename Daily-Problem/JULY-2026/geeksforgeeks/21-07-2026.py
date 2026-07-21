# Maximum Reachable Index Difference

class Solution:
    def maxIndexDifference(self, s):
        # code here
        n = len(s)
        best = [-1] * 26
        ans = -1

        for i in range(n - 1, -1, -1):
            farthest = i
            idx = ord(s[i]) - ord('a')

            if idx < 25 and best[idx + 1] != -1:
                farthest = best[idx + 1]

            best[idx] = max(best[idx], farthest)

            if s[i] == 'a':
                ans = max(ans, farthest - i)

        return ans
