# Binary Searchable Count

class Solution:
    def binarySearchable(self, arr):
        n = len(arr)
        searchable_cnt = 0
        
        for num in arr :
            left = 0
            right = n - 1
            
            while left <= right :
                mid = left + (right - left) // 2
                
                if arr[mid] == num :
                    searchable_cnt += 1
                    break
                elif arr[mid] < num :
                    left = mid + 1
                else :
                    right = mid - 1
                    
        return searchable_cnt
        
