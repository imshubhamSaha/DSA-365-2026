# Top View of Binary Tree


'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        if not root:
            return []
            
        q = deque([(root, 0)])
        top_nodes = {}
        
        while q:
            node, hd = q.popleft()
            
            if hd not in top_nodes:
                top_nodes[hd] = node.data
                
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        result = []
        for hd in sorted(top_nodes):
            result.append(top_nodes[hd])
            
        return result
        
        
