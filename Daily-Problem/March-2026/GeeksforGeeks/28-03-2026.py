# Articulation Point - II

from collections import defaultdict
class Solution:
    def articulationPoints(self, V, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        t = [0]
        disconnected = [-1] * V
        low = [-1] * V   
        seen = [False] * V
        prnt = [-1] * V
        ap = set()  

        def dfs(u):
            children = 0
            seen[u] = True
            disconnected[u] = low[u] = t[0]
            t[0] += 1

            for v in graph[u]:
                if not seen[v]:
                    prnt[v] = u
                    children += 1
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    if prnt[u] == -1 and children > 1:
                        ap.add(u)
                    if prnt[u] != -1 and low[v] >= disconnected[u]:
                        ap.add(u)
                elif v != prnt[u]:
                    low[u] = min(low[u], disconnected[v])
        for i in range(V):
            if not seen[i]:
                dfs(i)

        return sorted(list(ap)) if ap else [-1]
