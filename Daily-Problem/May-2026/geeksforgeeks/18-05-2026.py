# Maximum Sum Problem
class Solution:
    def maxSum(self, n):
        if n <=1 :
            return n
        return max(n , self.maxSum(n//2) + self.maxSum(n//3) + self.maxSum(n//4))
