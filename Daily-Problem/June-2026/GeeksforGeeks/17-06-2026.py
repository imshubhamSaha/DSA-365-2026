# Cut rope to maximise product

class Solution:
    def maxProduct(self, n):
        if n <= 3:
            return n - 1
            
        product = 1
        
        dup = n
        
        while dup > 4 :
            product *= 3
            dup -= 3
            
        return dup * product

        
        
        
