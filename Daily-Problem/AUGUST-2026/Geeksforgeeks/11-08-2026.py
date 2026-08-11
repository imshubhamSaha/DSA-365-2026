# Largest Odd Squares with Limited 1s
class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        n = len(mat)
        m = len(mat[0])

        pref = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                pref[i + 1][j + 1] = (
                    mat[i][j]
                    + pref[i][j + 1]
                    + pref[i + 1][j]
                    - pref[i][j]
                )

        def get_sum(r1, c1, r2, c2):
            return (
                pref[r2 + 1][c2 + 1]
                - pref[r1][c2 + 1]
                - pref[r2 + 1][c1]
                + pref[r1][c1]
            )

        ans = []

        for r, c in queries:

            if mat[r][c] > k:
                ans.append(-1)
                continue

            max_d = min(
                r,
                n - 1 - r,
                c,
                m - 1 - c
            )

            low = 0
            high = max_d
            best_d = 0

            while low <= high:
                mid = (low + high) // 2

                ones_count = get_sum(
                    r - mid,
                    c - mid,
                    r + mid,
                    c + mid
                )

                if ones_count <= k:
                    best_d = mid
                    low = mid + 1
                else:
                    high = mid - 1

            ans.append(2 * best_d + 1)

        return ans
