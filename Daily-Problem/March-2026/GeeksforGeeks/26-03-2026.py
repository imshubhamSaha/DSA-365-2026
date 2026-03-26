# Number of Ways to Arrive at Destination


import heapq
class Solution:
    def countPaths(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w)) 
        
    
        dist = [float('inf')] * V
        ways = [0] * V
        dist[0] = 0
        ways[0] = 1
        

        pq = [(0, 0)]  
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    ways[v] = ways[u]
                    heapq.heappush(pq, (dist[v], v))
                elif dist[u] + w == dist[v]:
                    ways[v] += ways[u]
        
        return ways[V-1]  
        
        
