#Minimum Elements Outside Subsequences
class Solution:
    def minCount(self, arr):
        """ code here """
        n = len(arr)
        dp = [[-1] * 101 for _ in range(101)]

        dp[0][0] = 0

        for x in arr:
            newdp = [row[:] for row in dp]

            for inc in range(101):
                for dec in range(101):
                    if dp[inc][dec] == -1:
                        continue

                    curr = dp[inc][dec]
                    if x > inc:
                        newdp[x][dec] = max(newdp[x][dec],curr + 1)

                    if x < dec or dec == 0:
                        newdp[inc][x] = max(newdp[inc][x],curr + 1)

                    newdp[inc][dec] = max(newdp[inc][dec],curr)

            dp = newdp

            max_selected = max(max(row) for row in dp)

        return n - max_selected
