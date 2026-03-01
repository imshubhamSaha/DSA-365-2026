# Move All Zeroes to End


class Solution:
	def pushZerosToEnd(self, arr):
    	n = len(arr)
    	left = 0
    	right = 0
    	
    	while right < n :
    	    if arr[right] != 0 :
    	        arr[left] = arr[right]
    	        left += 1
    	    right += 1
        
        while left < n :
            arr[left] = 0
            left += 1
        
        return arr
