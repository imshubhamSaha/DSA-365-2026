# Non-Attacking Black and White Knights

class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        total_squares = n * m

        # Total ways to place black and white knights
        total_ways = total_squares * (total_squares - 1)

        # Number of attacking placements
        attacking = 4 * (
            (n - 1) * max(0, m - 2) +
            (n - 2) * max(0, m - 1)
        )

        return total_ways - attacking
        
