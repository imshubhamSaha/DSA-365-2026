# 1886. Determine Whether Matrix Can Be Obtained By Rotation

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        rotation_happened = [True] * 4

        for i in range(n) :
            for j in range(n) :
                if mat[i][j] != target[i][j] :
                    rotation_happened[0] = False
                if mat[i][j] != target[j][n-i-1] :
                    rotation_happened[1] = False
                if mat[i][j] != target[n-i-1][n-j-1] :
                    rotation_happened[2] = False
                if mat[i][j] != target[n-j-1][i] :
                    rotation_happened[3] = False

        return rotation_happened[0] or rotation_happened[1] or rotation_happened[2] or rotation_happened[3]
