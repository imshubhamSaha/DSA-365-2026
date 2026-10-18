# Shortest Path From 1 To n
class Solution:
    def minimumStep (self, n):
        # code here
        ret = -1
        while n:
            ret +=1
            if n % 3 == 0:
                n //=3
            else:
                n -= 1
        return ret
