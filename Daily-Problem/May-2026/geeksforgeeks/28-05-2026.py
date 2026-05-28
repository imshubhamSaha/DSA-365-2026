# Vertical Sum

# Structure of binary tree node
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
'''

class Solution:
    def verticalSum(self, root):
        mp = {}

        self.mn = 0
        self.mx = 0

        def dfs(node, hd):
            if not node:
                return

            mp[hd] = mp.get(hd, 0) + node.data

            self.mn = min(self.mn, hd)
            self.mx = max(self.mx, hd)

            dfs(node.left, hd - 1)
            dfs(node.right, hd + 1)

        dfs(root, 0)

        ans = []

        for i in range(self.mn, self.mx + 1):
            ans.append(mp[i])

        return ans
        
