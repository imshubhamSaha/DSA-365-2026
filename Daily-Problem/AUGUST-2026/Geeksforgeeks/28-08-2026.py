# Minimum Cost Selection
class Solution:

    def minCost(self, mat):
        n = len(mat)
        if n == 1:
            return min(mat[0])
        a, b, c = mat[0][0], mat[0][1], mat[0][2]
        for row in range(1, len(mat)):
            d = mat[row][0] + min(b, c)
            e = mat[row][1] + min(a, c)
            f = mat[row][2] + min(a, b)
            a, b, c = d, e, f

        return min(a, b, c)
