# 1260. Shift 2D Grid
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        dup_k = k % (n * m)

        while dup_k > 0 :
            for i in range(n) :
                for j in range(1, m) :
                    temp = grid[i][j]
                    grid[i][j] = grid[i][0]
                    grid[i][0] = temp

            for i in range(1,n) :
                temp = grid[i][0]
                grid[i][0] = grid[0][0]
                grid[0][0] = temp
            dup_k -= 1

        return grid
