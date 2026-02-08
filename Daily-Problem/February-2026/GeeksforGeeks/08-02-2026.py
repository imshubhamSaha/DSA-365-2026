# Maximum Product Subarray


class Solution:
	def maxProduct(self,arr):
		n = len(arr)
        maxi = arr[0]
        mini = arr[0]
        maxProd = arr[0]
        
        for i in range(1, n) :
            if arr[i] < 0 :
                t = maxi
                maxi = mini
                mini = t
            
            maxi = max(arr[i], maxi * arr[i])
            mini = min(arr[i], mini * arr[i])
            
            maxProd = max(maxProd, maxi)
        
        
        return maxProd
