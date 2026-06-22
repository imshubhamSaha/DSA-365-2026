# Maximum Area Between Bars


class Solution:
    def maxArea(self, height):
        n = len(height)
        area = 0
        
        right = n - 1
        left =  0
        
        while left < right :
            left_height = height[left]
            right_height = height[right]
            
            area = max(area, (right - left - 1) * min(left_height, right_height))
            if left_height < right_height :
                left += 1
            else :
                right -= 1
            
        return area
        
        
