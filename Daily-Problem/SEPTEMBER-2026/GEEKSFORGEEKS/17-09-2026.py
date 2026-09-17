# Min Edge Reversals for Path
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        # code here
        g = defaultdict(list)
        for frm, to in edges:
            g[frm].append((to, 0))
            g[to].append((frm, 1))

        costs = [float('inf')]*(n+1)
        costs[src] = 0

        q = [(0, src)]
        while q:
            cost0, v = heappop(q)
            if v == dst:
                return cost0
            for nbr, c in g[v]:
                cost = cost0+c
                if costs[nbr] > cost:
                    costs[nbr] = cost
                    heappush(q, (cost, nbr))
        return -1
