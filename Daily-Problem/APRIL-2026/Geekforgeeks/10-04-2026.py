#Sorted subsequence of size 3

class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3 :
            return []
            
        smallest = [0] * n
        greatest = [0] * n
        
        smallest[0] = arr[0]
        greatest[n-1] = arr[n-1]
        
        for i in range(1, n) :
            smallest[i] = min(smallest[i-1], arr[i])
            greatest[ n -1-i] = max(arr[n-1-i], greatest[n - i])
        
        
        for i in range(1, n) :
            if smallest[i] < arr[i] and greatest[i] > arr[i] :
                return [smallest[i], arr[i], greatest[i]]
                
        return []
            
            
