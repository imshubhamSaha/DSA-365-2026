# Substrings with more 1's than 0's
class Solution:
    def countSubstring(self, s):
        lenS = len(s)
        timesOfValue = [0]*(2*lenS + 1)
        i0 = lenS
        substrs = 0 
        currValue = 0
        ended = 0
        timesOfValue[i0] = 1
        for i in range(lenS):
            if(s[i]=='1'):
                ended += timesOfValue[i0+currValue]
                currValue += 1
            else:
                ended -= timesOfValue[i0+currValue-1]
                currValue -= 1            
            substrs += ended    
            timesOfValue[i0+currValue] +=1    
        return substrs
        
