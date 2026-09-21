# Check Level Anagrams in Binary Trees
"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""
from collections import deque
class Solution:

    def areAnagrams(self, root1, root2):
        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            size1 = len(q1)
            size2 = len(q2)

            if size1 != size2:
                return False

            freq1 = {}
            freq2 = {}

            for _ in range(size1):
                node = q1.popleft()
                freq1[node.data] = freq1.get(node.data, 0) + 1

                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)


            for _ in range(size2):
                node = q2.popleft()

                freq2[node.data] = freq2.get(node.data, 0) + 1
                if node.left:
                    q2.append(node.left)

                if node.right:
                    q2.append(node.right)

            if freq1 != freq2:
                return False

        return not q1 and not q2
        
