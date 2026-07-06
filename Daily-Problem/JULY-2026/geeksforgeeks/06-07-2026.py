# Max Sum Path in Two Arrays
class Solution:
    def maxPathSum(self, a, b):
        n = len(a)
        m = len(b)
        i = 0
        j = 0
        
        max_sum = 0
        left_arr_sum = 0
        right_arr_sum = 0
        
        while i < n and j < m :
            left_num = a[i]
            right_num = b[j]
            
            if left_num == right_num :
                max_sum += max(left_arr_sum, right_arr_sum)
                max_sum += left_num
                left_arr_sum = right_arr_sum = 0
                i += 1
                j += 1
            elif left_num < right_num :
                left_arr_sum += left_num
                i += 1
            else :
                right_arr_sum += right_num
                j += 1
        
        while i < n :
            left_arr_sum += a[i]
            i += 1
        
        while j < m :
            right_arr_sum += b[j]
            j += 1
            
        max_sum += max(left_arr_sum, right_arr_sum)
        
        return max_sum
                
