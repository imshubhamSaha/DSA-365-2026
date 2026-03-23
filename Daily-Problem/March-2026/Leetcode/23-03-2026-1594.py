# 1594. Maximum Non Negative Product in a Matrix

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = (10**9) + 7
        MAX, MIN = 0, 1

        ROWS, COLS = len(grid), len(grid[0])
        grid[0][0] = (grid[0][0], grid[0][0])

        for c in range(1, COLS):
            curr = grid[0][c] * grid[0][c - 1][MAX]
            grid[0][c] = (curr, curr)

        for r in range(1, ROWS):
            curr = grid[r][0] * grid[r - 1][0][MAX]
            grid[r][0] = (curr, curr)

        for r in range(1, ROWS):
            for c in range(1, COLS):
                all_products = [
                    grid[r][c] * grid[r][c - 1][MAX],
                    grid[r][c] * grid[r][c - 1][MIN],
                    grid[r][c] * grid[r - 1][c][MAX],
                    grid[r][c] * grid[r - 1][c][MIN],
                ]

                grid[r][c] = (max(all_products), min(all_products))

        if grid[ROWS - 1][COLS - 1][MAX] < 0:
            return -1

        return grid[ROWS - 1][COLS - 1][MAX] % MOD
