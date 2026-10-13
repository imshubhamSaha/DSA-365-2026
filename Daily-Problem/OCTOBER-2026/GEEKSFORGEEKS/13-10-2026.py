# Adding Ones
from itertools import accumulate
class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
        # code here
        arr = [0] * n
        for up in updates:
            arr[up - 1] += 1

        psum = list(accumulate(arr))
        return psum
