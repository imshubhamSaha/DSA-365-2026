# Split Array into Minimum Subsets
class Solution:
    def minSubsets(self, arr):
        n = len(arr)
        mpp = {}
        
        for num in arr :
            mpp[num] = 1
            
        consecutive_subset = 0
        
        idx = 0
        
        while idx < n :
            idx += 1
            if (arr[idx - 1] - 1) in mpp :
                continue
            consecutive_subset += 1
                
        return consecutive_subset
            
