# Wifi Range

class Solution:
    def wifiRange(self, s, x):
        n = len(s)
        
        last_range = -1
        idx = 0
        
        while idx < n :
            if s[idx] == '1' :
                left_range = idx - x 
                right_range = idx + x
                if ((last_range != -1 and left_range > (last_range + 1)) or 
                (last_range == -1 and left_range > 0)):
                    return False
                last_range = right_range
            idx += 1
        
            
        return False if last_range < (n - 1) else True
