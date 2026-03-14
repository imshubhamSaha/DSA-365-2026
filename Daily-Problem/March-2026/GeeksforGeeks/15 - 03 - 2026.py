# Vertical Tree Traversal


'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root):
        # code here
        if not root:
            return []
        hd_map = defaultdict(list)
        queue = deque([(root, 0)])
        min_hd, max_hd = 0, 0
        while queue:
            node, hd = queue.popleft()
            hd_map[hd].append(node.data)
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        result = []
        for i in range(min_hd, max_hd + 1):
            if i in hd_map:
                result.append(hd_map[i])
        return result
        
