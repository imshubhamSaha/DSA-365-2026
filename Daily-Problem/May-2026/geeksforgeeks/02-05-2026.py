# Position of the Set Bit

class Solution:
    def findPosition(self, n):
        pos = -1
        num = n
        p = 1
        while num :
            if (num & 1) :
                if pos != -1 :
                    return -1
                pos = p
            p += 1
            num >>= 1
        
        return pos 
