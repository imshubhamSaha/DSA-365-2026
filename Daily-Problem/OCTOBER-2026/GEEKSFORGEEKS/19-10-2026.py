# Count Indices That Escape Array
from collections import deque
class Solution:
    def goodIndices(self, arr):
        # code here
        n = len(arr)
        rev = {i: [] for i in range(n)}
        good_starts = []
        for i in range(n):
            nxt = i + arr[i]
            if 0 <= nxt < n:
                rev[nxt].append(i)
            else:
                good_starts.append(i)

        q = deque(good_starts)
        good = set(good_starts)
        while q:
            node = q.popleft()
            for parent in rev[node]:
                if parent not in good:
                    good.add(parent)
                    q.append(parent)
        return len(good)
