# Product Pair

class Solution:
    def isProduct(self, arr, target):
        n = len(arr)
        seen = set()
        
        for num in arr :
            if num == 0 and target == 0 :
                return True
            if num == 0 :
                continue
            required = target / num 
            if required in seen :
                return True
            seen.add(num)
        
        return False
