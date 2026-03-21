# 3643. Flip Square Submatrix Vertically

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        l = min(y + k, n)
        top = x
        bottom = min((x + k - 1), m - 1)

        while top < bottom :
            for i in range(y, l) :
                temp = grid[top][i]
                grid[top][i] = grid[bottom][i]
                grid[bottom][i] = temp
            top += 1
            bottom -= 1

        return grid
