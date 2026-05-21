# Check if All Bits Set

class Solution:
    def isBitSet(self, n):
        return (n & 1) == 1 and (n & (n + 1)) == 0
