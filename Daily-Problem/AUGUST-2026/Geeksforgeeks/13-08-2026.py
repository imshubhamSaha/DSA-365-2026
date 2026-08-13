# Longest Path in a Directed Acyclic Graph
from collections import defaultdict
class Solution:
    def maxDistance(self, V, src, edges):
        node_edges = defaultdict(list)
        for u,v,w in edges:
            node_edges[u].append((v, w))
        res = ['INF']*V
        q = {src}
        res[src] = 0
        while q:
            node_from = q.pop()
            for node_to,w in node_edges[node_from]:
                if res[node_to]=='INF' or res[node_to] < res[node_from] + w:
                    res[node_to] = res[node_from] + w
                    q.add(node_to)
        return res
 

