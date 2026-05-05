# Sum of XOR of all pairs

class Solution:
    def sumXOR(self, arr):
        n, total = len(arr), 0
        for i in range(32):
            count1 = sum((num >> i) & 1 for num in arr)
            total += count1 * (n - count1) * (1 << i)
        return total
