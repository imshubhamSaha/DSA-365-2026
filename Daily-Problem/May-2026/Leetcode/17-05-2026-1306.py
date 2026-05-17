# 1306. Jump Game III
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=deque()
        visited=set()
        q.append(start)
        while(q):
            i=q.popleft()
            if(arr[i]==0):
                return True
            if(i in visited):
                continue
            visited.add(i)
            l=i-arr[i]
            r=i+arr[i]
            if(l>=0):
                q.append(l)
            if(r<len(arr)):
                q.append(r)
        return False
