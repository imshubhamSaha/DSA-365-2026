# Minimum Absolute Difference In BST
'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
        # code here
        self.res = self.prev = float('inf')

        def dfs(node):
            if node:
                dfs(node.left)
                self.res = min(self.res, abs(node.data - self.prev))
                self.prev = node.data
                dfs(node.right)

        dfs(root)
        return self.res
