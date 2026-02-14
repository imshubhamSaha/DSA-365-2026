# The Painter's Partition Problem-II


class Solution:
    def minTime (self, arr, k):
        def is_possible(max_time):
            painters = 1
            total = 0
            
            for board in arr:
                total += board
                
                if total > max_time:
                    painters += 1
                    total = board
                    
                    if painters > k:
                        return False
                        
            return True
        
        low = max(arr)
        high = sum(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if is_possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
        
