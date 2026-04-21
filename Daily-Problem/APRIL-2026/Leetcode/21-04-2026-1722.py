# 1722. Minimize Hamming Distance After Swap Operations
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = [i for i in range(len(source))]

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            parent[find(v)]=find(u)

        for i, j in allowedSwaps:
            union(i, j)    

        components = defaultdict(lambda: defaultdict(int))

        for i in range(len(source)):
            components[find(i)][source[i]]+=1
        ans = 0
        for index in range(len(source)):
            
            if components[find(index)][target[index]] > 0:
                components[find(index)][target[index]] -= 1
            else:
                ans += 1    
        return ans            
