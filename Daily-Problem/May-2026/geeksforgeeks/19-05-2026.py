# Minimum Multiplications to reach End

from collections import deque
class Solution:
    def minSteps(self, arr, start, end):
        q = deque()
        q.append((start, 0)) # strat, steps
        
        visited = set()
        visited.add(start)
        
        while q:
            val, steps = q.popleft()
            
            if val == end:
                return steps
                
            for num in arr:
                new_val = (val * num)%1000
                
                if new_val in visited:
                    continue
                
                visited.add(new_val)
                q.append((new_val, steps+1))
                
                
        return -1
