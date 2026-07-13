# Rearrange the Array

from math import gcd
class Solution:
    def minOperations(self, b):
        M = 10**9 + 7
        n = len(b)
        visited = [False]*(n+1)
        
        lcm = 1
        for i in range(1, n+1):
            if not visited[i]:
                cur = i
                cycle_length = 0
                while not visited[cur]:
                    visited[cur] = True
                    cur = b[cur-1]
                    cycle_length += 1
                lcm = lcm*cycle_length//gcd(lcm, cycle_length)
        
        return lcm%M
        
