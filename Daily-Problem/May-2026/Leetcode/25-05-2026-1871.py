#1871. Jump Game VII
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if int(s[-1]): return False

        dp = [False] * n
        dp[0] = True
        reach, max_range = 0, maxJump

        for i in range(minJump, n):
            if i > max_range: return False

            reach += dp[i - minJump]

            if i > maxJump:
                reach -= dp[i - maxJump - 1]

            if reach and not int(s[i]):
                dp[i] = True
                max_range = i + maxJump

        return reach > 0
