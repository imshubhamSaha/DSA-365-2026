#Elements in the Range

class Solution:
    def checkElements(self, start, end, arr):
        n = len(arr)
        count  = 0
        for num in arr :
            if (num >= start and num <= end) :
                count += 1
            
                
        return count == (end - start + 1)
        
