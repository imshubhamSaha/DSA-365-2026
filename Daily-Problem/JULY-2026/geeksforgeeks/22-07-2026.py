# Minimum Deletions to Make Sorted
class Solution:
    def findLstIdx(self, last_index, num) :
        low = 0
        high = len(last_index) - 1
        res = -1
        while low <= high :
            mid = low + (high - low) // 2
            if last_index[mid] >= num :
                res = mid
                high = mid - 1
            else :
                low = mid + 1
        
        return res
        
    def minDeletions(self, arr):
        n = len(arr)
        last_index = []
        
        for i in range(n) :
            num = arr[i]
            
            if len(last_index) == 0 or last_index[-1] < num :
                last_index.append(num)
            else :
                idx = self.findLstIdx(last_index, num)
                last_index[idx] = num
                
        return n - len(last_index)
        
