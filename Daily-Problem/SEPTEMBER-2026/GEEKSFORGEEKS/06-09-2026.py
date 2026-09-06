# Sum of Pairwise ANDs
class Solution:
    def pairAndSum(self, arr):
        # code here
        if not arr:
            return 0
        n = len(arr)
        result = 0
        for bit in range(max(arr).bit_length()):
            set_bits = sum((value >> bit) & 1 for value in arr)
            result += (1 << bit) * set_bits * (set_bits - 1) // 2

        return result
