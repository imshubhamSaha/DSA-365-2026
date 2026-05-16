#Not a subset sum

class Solution:
    def findSmallest(self, arr):
        arr.sort()
        n = len(arr)
        result = 1
        
        for num in arr :
            if result >= num :
                result += num
            
        return result
