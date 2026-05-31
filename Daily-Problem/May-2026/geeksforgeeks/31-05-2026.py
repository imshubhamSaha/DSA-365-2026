# Express as Consecutive Number Sum

class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        if (n & (n - 1)) == 0:
            return False
        return True
        
        
