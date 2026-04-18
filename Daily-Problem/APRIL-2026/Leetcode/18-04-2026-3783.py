# 3783. Mirror Distance of an Integer

class Solution:
    def rev(Self, n : int) -> int :
        rev_number = 0
        while n :
            rev_number = rev_number * 10 + n % 10
            n //= 10
        
        return rev_number

    def mirrorDistance(self, n: int) -> int:
        if n <= 9 :
            return 0
        return abs(self.rev(n) - n)
