#796. Rotate String

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if n != m :
            return False
        
        for i in range(n) :
            idx = i
            j = 0
            while j < n :
                if s[idx%n] != goal[j] :
                    break
                idx += 1
                j += 1
            if j == n :
                return True
        
        return False
T C : O(n * n)
S C : O(1)


----------------------------------------------------


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if n != m :
            return False

        lps = self.build_lps(goal)
        j = 0
        for i in range(2 * n):
            while j > 0 and s[i % n] != goal[j]:
                j = lps[j - 1]
            
            if s[i % n] == goal[j]:
                j += 1
            
            if j == n:
                return True
        
        return False


    def build_lps(self, pattern):
        lps = [0] * len(pattern)
        j = 0
        
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
        
        return lps


    
