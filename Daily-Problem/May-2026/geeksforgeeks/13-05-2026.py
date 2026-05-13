# Mother Vertex

from collections import defaultdict
class Solution:
    def findMotherVertex(self, V, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        
        def dfs(node, visited):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, visited)


        visited = [False] * V
        candidate = -1

        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                candidate = i

        visited = [False] * V
        dfs(candidate, visited)

        if not all(visited):
            return -1

        ans = candidate
        for i in range(candidate):
            visited = [False] * V
            dfs(i, visited)
            if all(visited):
                ans = i
                break

        return ans
