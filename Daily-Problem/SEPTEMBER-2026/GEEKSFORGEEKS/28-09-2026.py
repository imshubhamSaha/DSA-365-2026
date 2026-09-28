# Range GCD Queries
from math import gcd
class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        
        n = len(arr)

        size = 1
        while size < n:
            size *= 2
        
        seg = [0] * (2 * size)

        for i in range(n):
            seg[size + i] = arr[i]

        for i in range(size - 1, 0, -1):
            seg[i] = gcd(seg[2 * i], seg[2 * i + 1])

        def update(index, value):
            pos = size + index
            seg[pos] = value

            pos //= 2
            while pos:
                seg[pos] = gcd(seg[2 * pos], seg[2 * pos + 1])
                pos //= 2

        def range_gcd(l, r):
            l += size
            r += size

            result_left = 0
            result_right = 0

            while l <= r:
                if l % 2 == 1:
                    result_left = gcd(result_left, seg[l])
                    l += 1

                if r % 2 == 0:
                    result_right = gcd(seg[r], result_right)
                    r -= 1

                l //= 2
                r //= 2

            return gcd(result_left, result_right)

        ans = []

        for query in queries:
            if query[0] == 0:
                l, r = query[1], query[2]
                ans.append(range_gcd(l, r))
            else:
                index, value = query[1], query[2]
                update(index, value)

        return ans
