# Largest BST


class Solution:
    def largestBst(self, root):
        mx=0
        def dfs(cur=root):
            nonlocal mx
            if not cur:
                return False,None,None,None
            if not cur.left and not cur.right:
                mx=max(mx,1)
                return True,cur.data,cur.data,1
            lok,lmn,lmx,lsz=dfs(cur.left)
            rok,rmn,rmx,rsz=dfs(cur.right)
            if lok and rok and lmx<cur.data<rmn:
                mx=max(mx,lsz+1+rsz)
                return True,lmn,rmx,lsz+1+rsz
            if lok and not cur.right and lmx<cur.data:
                mx=max(mx,lsz+1)
                return True,lmn,cur.data,lsz+1
            if not cur.left and rok and cur.data<rmn:
                mx=max(mx,rsz+1)
                return True,cur.data,rmx,rsz+1
            return False,None,None,None
        dfs()
        return mx
