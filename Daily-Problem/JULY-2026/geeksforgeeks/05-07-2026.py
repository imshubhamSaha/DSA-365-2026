# Max Gap Between Two Same
class Solution:

    def maxCharGap(self, s: str) -> int:
        n = len(s)
        max_gap = -1
        char_pos = [-1] * 26
        for i in range(n) :
            char_idx = ord(s[i]) - ord('a')
            if char_pos[char_idx] != -1 :
                max_gap = max(max_gap, (i - char_pos[char_idx]))
            else :
                char_pos[char_idx] = i + 1 
        
        return max_gap
