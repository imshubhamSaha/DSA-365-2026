# Minimum cost to connect all houses in a city

#User function Template for python3
import heapq
class Solution:
    def minCost(self, houses):
        n = len(houses)
        seen = [False] * n
        minimum_cost = [float('inf')] * n
        minimum_cost[0] = 0
        heap = [(0, 0)]  
        cost_to_connect = 0
        
        while heap:
            cost, u = heapq.heappop(heap)
            if seen[u]:
                continue
            
            seen[u] = True
            cost_to_connect += cost
            
            for v in range(n):
                if not seen[v]:
                    dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    if dist < minimum_cost[v]:
                        minimum_cost[v] = dist
                        heapq.heappush(heap, (dist, v))
                        
        return cost_to_connect
