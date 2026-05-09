# Count Spanning Trees in a Graph


class Solution:
    def countSpanTree(self, n, edges):
        # code here
        if n == 1:
            return 1

       
        lap = [[0] * n for _ in range(n)]

        for u, v in edges:
            lap[u][u] += 1
            lap[v][v] += 1
            lap[u][v] -= 1
            lap[v][u] -= 1

      
        mat = [row[1:] for row in lap[1:]]

        def determinant(matrix, size):
            mat = [row[:] for row in matrix]
            det = 1

            for i in range(size):

                pivot = i
                for j in range(i, size):
                    if abs(mat[j][i]) > abs(mat[pivot][i]):
                        pivot = j

                if mat[pivot][i] == 0:
                    return 0

                if pivot != i:
                    mat[i], mat[pivot] = mat[pivot], mat[i]
                    det *= -1

                det *= mat[i][i]

                for j in range(i + 1, size):
                    factor = mat[j][i] / mat[i][i]

                    for k in range(i, size):
                        mat[j][k] -= factor * mat[i][k]

            return round(det)

        return determinant(mat, n - 1)
