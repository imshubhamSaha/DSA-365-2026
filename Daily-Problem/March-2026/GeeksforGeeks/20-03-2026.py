# Predecessor and Successor

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        self.pre = None
        self.suc = None

        def inorder_search(node):
            if not node:
                return
            if node.data < key:
                self.pre = node
                inorder_search(node.right)
            elif node.data > key:
                self.suc = node
                inorder_search(node.left)
            else:
                if node.left:
                    temp = node.left
                    while temp.right:
                        temp = temp.right
                    self.pre = temp
                if node.right:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    self.suc = temp

        inorder_search(root)
        return (self.pre, self.suc)
