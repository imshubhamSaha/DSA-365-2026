# 1840. Maximum Building Height

class Solution:
    def maxBuilding(self, n: int, restr: List[List[int]]) -> int:
        restr.append([1, 0])
        restr.sort()
        m = len(restr)

        def yCap(x1, y1, x2, y2):
            return min(y2, y1 + abs(x2 - x1))

        def yPeak(x1, y1, x2, y2):
            return (y1 + y2 + x2 - x1) >> 1
        
        for i in range(1, m):
            restr[i][1] = yCap(*restr[i - 1], *restr[i])

        for i in range(m - 2, -1, -1):
            restr[i][1] = yCap(*restr[i + 1], *restr[i])

        res = 0
        for i in range(1, m):
            res = max(res, yPeak(*restr[i - 1], *restr[i]))

        return max(res, restr[-1][1] + n - restr[-1][0])
