# Successful Binary Searches Irrespective of Pivot
class Solution:
    def countAlwaysFound(self, arr):
        # code here
        from itertools import accumulate
        n = len(arr)
        prefix_max = list(accumulate(arr, max, initial = 0))
        suffix_min, count = arr[-1] + 1, 0
        for i in range(n - 1, -1, -1):
            if arr[i] < suffix_min:
                suffix_min = arr[i]
                if prefix_max[i] < arr[i]:
                    count += 1
        return count
