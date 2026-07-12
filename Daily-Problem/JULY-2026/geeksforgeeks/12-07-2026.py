# Max Amount by Selling K Tickets

import heapq
class Solution:
    def maxAmount(self, arr, k):
        pq = []
        mod = int(1e9)+7
        for ele in arr:
            heapq.heappush(pq,-ele)
        ans=0
        while k>0:
            ele = -heapq.heappop(pq)
            if ele<=0:
                return ans
            ans = (ans+ele)%mod
            heapq.heappush(pq,-(ele-1))
            k-=1
        return ans
 

