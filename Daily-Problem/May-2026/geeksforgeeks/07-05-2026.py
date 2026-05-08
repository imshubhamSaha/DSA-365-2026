# Check if subtree

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def isIdentical(self,r1,r2) :
        if not r1 and not r2 :
            return True
        if not r1 or not r2 :
            return False
        
        return (r1.data == r2.data and self.isIdentical(r1.left,r2.left) and self.isIdentical(r1.right,r2.right))
        
    def isSubTree(self, root1, root2):
        if not root1 :
            return False
        
        if not root2 :
            return False
            
        if self.isIdentical(root1 , root2) :
            return True
        return self.isSubTree(root1.left, root2) or self.isSubTree(root1.right, root2)
        
   
