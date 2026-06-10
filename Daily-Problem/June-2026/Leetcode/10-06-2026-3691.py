# 3691. Maximum Total Subarray Value II

import heapq

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.maxV = [0] * (4 * self.n)
        self.minV = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, nums)

    def build(self, node, l, r, nums):
        if l == r:
            self.maxV[node] = self.minV[node] = nums[l]
            return
        m = l + (r - l) // 2
        self.build(2 * node, l, m, nums)
        self.build(2 * node + 1, m + 1, r, nums)
        self.minV[node] = min(self.minV[2 * node], self.minV[2 * node + 1])
        self.maxV[node] = max(self.maxV[2 * node], self.maxV[2 * node + 1])

    def queryMax(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.maxV[node]
        m = l + (r - l) // 2
        res = float('-inf')
        if ql <= m:
            res = max(res, self.queryMax(2 * node, l, m, ql, qr))
        if qr > m:
            res = max(res, self.queryMax(2 * node + 1, m + 1, r, ql, qr))
        return res

    def queryMin(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.minV[node]
        m = l + (r - l) // 2
        res = float('inf')
        if ql <= m:
            res = min(res, self.queryMin(2 * node, l, m, ql, qr))
        if qr > m:
            res = min(res, self.queryMin(2 * node + 1, m + 1, r, ql, qr))
        return res

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sg = SegmentTree(nums)
        
        pq = []
        for i in range(n):
            val = sg.queryMax(1, 0, n - 1, i, n - 1) - sg.queryMin(1, 0, n - 1, i, n - 1)
            heapq.heappush(pq, (-val, i, n - 1))
            
        ans = 0
        for _ in range(k):
            if not pq:
                break
            neg_val, l, r = heapq.heappop(pq)
            ans += (-neg_val)
            
            if r > l:
                val = sg.queryMax(1, 0, n - 1, l, r - 1) - sg.queryMin(1, 0, n - 1, l, r - 1)
                heapq.heappush(pq, (-val, l, r - 1))
                
        return ans
