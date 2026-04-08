#Segregate 0s and 1s

class Solution:
    def segregate0and1(self, arr):
        n = len(arr)
        left = 0
        right = n - 1
        
        
        while (left < right) :
            if arr[left] == 1 :
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                right -= 1
                left -= 1
            left += 1
            
        return arr
