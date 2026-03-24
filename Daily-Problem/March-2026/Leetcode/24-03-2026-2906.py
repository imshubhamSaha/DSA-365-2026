# 2906. Construct Product Matrix

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        zero = 0
        total = 1
        mod = 12345
        for i in range(n):
            for j in range(m):
                grid[i][j] %= mod
                if grid[i][j] == 0:
                    zero += 1
                else:
                    total = total * grid[i][j]

        for i in range(n):
            for j in range(m):
                if zero > 1:
                    grid[i][j] = 0
                elif zero == 1:
                    if grid[i][j]:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = total % mod
                else:
                    grid[i][j] = (total // grid[i][j]) % mod
        return grid
