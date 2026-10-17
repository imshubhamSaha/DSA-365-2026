# Convert One String to Another with Constraints
class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        # code here
        n, m = len(s1), len(s2)
        if n != m :
            return False
        a = b = 0
        for i in range(n):
            if s1[i]=='A':
                a += 1
            elif s1[i]=='B':
                b += 1
            if s2[i]=='A':
                a -= 1
            elif s2[i]=='B':
                b -= 1
            if a > 0 or b < 0 or a * b < 0:
                return False
        
        return True
        
