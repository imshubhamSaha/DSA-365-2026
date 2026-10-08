# Minimum Operations to Reach n
class Solution:
    def minOperation(self, n):
        # code here
        count = 0
        temp = n
        while temp > 0 :
            if temp % 2 == 0 :
                temp //= 2
            else :
                temp -= 1
            
            count += 1
        
        return count
