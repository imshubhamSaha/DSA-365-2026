# 628. Maximum Product of Three Numbers
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = b = c = -1001
        x = y = 1001
        for num in nums:
            pa, pb, px = a, b, x
            
            a = max(a, num)
            b = max(b, min(pa, num))
            c = max(c, min(pb, num))
            
            x = min(x, num)
            y = min(y, max(px, num))

        
        return max((a * b * c), a * x * y)
