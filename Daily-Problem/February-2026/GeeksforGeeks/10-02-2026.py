# Koko Eating Bananas


class Solution:
    def kokoEat(self, arr, k):
        def can_finish(speed):
            hours = 0
            for bananas in arr:
                hours += math.ceil(bananas / speed)
            return hours <= k

        left, right = 1, max(arr)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                result = mid
                right = mid - 1  
            else:
                left = mid + 1  

        return result
        
