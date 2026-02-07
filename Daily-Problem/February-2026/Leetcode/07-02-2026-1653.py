# 1653. Minimum Deletions to Make String Balanced
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        b_occurence = 0
        removed = 0

        for i in range(n) :
            if s[i] == 'b' :
                b_occurence += 1
            elif b_occurence and s[i] == 'a':
                b_occurence -= 1
                removed += 1
        
        return removed  
