# Minimum Insert and Delete to Convert

import bisect
class Solution:
    
    def minInsAndDel(self, a, b):
        n = len(a)
        m = len(b)
        b_set = set(b)
        lis = []
        for i in range(n):
            if a[i] in b_set:
                idx = bisect.bisect_left(lis, a[i])
                if idx == len(lis):
                    lis.append(a[i])
                else:
                    lis[idx] = a[i]
        return n + m - 2 * len(lis)


        
