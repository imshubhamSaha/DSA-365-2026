# Lexicographically smallest after removing k

class Solution:
    def lexicographicallySmallest(self, s, k):
        # code here 
        n = len(s)
        
        k = k // 2 if (n & (n - 1)) == 0 else k * 2
        if k >= n :
            return -1
        
        stk = []
        to_removed = k
        
        for i in range(n):
            ch = s[i]
            while stk and stk[-1] > ch and to_removed > 0 :
                stk.pop()
                to_removed -= 1
            stk.append(ch)
            
        
        while to_removed > 0 :
            stk.pop()
            to_removed -= 1
            
        return ''.join(stk)
