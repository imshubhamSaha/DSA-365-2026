# Visit Leaves with Budget
''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        # code here
        from collections import Counter
        cnt=Counter()
        def dfs(cur=root,lvl=1):
            nonlocal cnt
            if not cur:
                return
            if not cur.left and not cur.right:
                cnt[lvl]+=1
                return
            dfs(cur.left,lvl+1)
            dfs(cur.right,lvl+1)
        dfs()
        ret=0
        for l in sorted(cnt):
            while k>=l:
                k-=l
                cnt[l]-=1
                ret+=1
                if cnt[l]==0:
                    break
        return ret
