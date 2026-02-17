# Maximum number of overlapping Intervals



class Solution:
    def overlapInt(self, arr):
        maxi=-1
        for i in arr:
            maxi=max(maxi,i[1])
        
        prefix=[0]*(maxi+1)
        
        for ra in arr:
            prefix[ra[0]-1]+=1
            prefix[ra[1]]-=1
        prev=0  
        ans=-1
        for i in range(maxi+1):
            prefix[i]+=prev
            prev=prefix[i]
            ans=max(ans,prefix[i])
        return ans
        
