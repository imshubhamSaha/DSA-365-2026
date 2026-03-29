#2839. Check if Strings Can be Made Equal With Operations I
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)

        for i in range(n) :
            if (s1[i] != s2[i]) and (s1[i] != s2[(i + 2) % 4]) :
                return False
        
        return True
