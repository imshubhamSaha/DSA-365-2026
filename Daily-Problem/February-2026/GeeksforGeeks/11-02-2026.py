# Equalize the Towers


class Solution:
    def minCost(self, heights, cost):
        def calc(m):
            res=0
            for i,h in enumerate(heights):
                res+=abs(h-m)*cost[i]
            return res
            
        low=min(heights)
        high=max(heights)
        res=float('inf')
        while(low<=high):
            mid=(low+high)//2
            c1=calc(mid-1)
            c2=calc(mid)
            c3=calc(mid+1)
            if c1>=c2<=c3:
                res=c2
                break
            elif(c1>=c2>=c3):
                low=mid+1
            else:
                high=mid-1
        return res
        
