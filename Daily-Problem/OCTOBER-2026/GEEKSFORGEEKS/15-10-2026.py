# Maximum Without 3 Consecutive Set Bits
class Solution:

    def maxValue(self, n: int) -> int:
        """code here"""
        i = n.bit_length() - 1

        while i >= 2:
            first = (n >> i) & 1
            second = (n >> (i - 1)) & 1
            third = (n >> (i - 2)) & 1

            if first == second == third == 1:
                n &= ~(1 << (i - 2))
                i = min(i - 1, n.bit_length() - 1)
            else:
                i -= 1

        return n
