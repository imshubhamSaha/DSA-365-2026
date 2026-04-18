# Flip to Maximize 1s

class Solution:
    def maxOnes(self, arr):
        ones_cnt = 0
        zeros_cnt = 0
        mx_flip_one = 0
        
        for num in arr :
            if num == 1 :
                ones_cnt += 1
                zeros_cnt -= 1
            else :
                zeros_cnt += 1
                mx_flip_one = max(mx_flip_one, zeros_cnt)
            
            if zeros_cnt < 0 :
                zeros_cnt = 0
        
        return ones_cnt + mx_flip_one
        
