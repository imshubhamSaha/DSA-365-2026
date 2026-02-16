# Meeting Rooms


class Solution:
    def canAttend(self, arr):
        n = len(arr)
        arr.sort()
        
        for meet in range(1,  n) :
            if arr[meet][0] < arr[meet-1][1] :
                return False
                
        return True
