# Smallest window containing 0, 1 and 2


class Solution:
    def checkValidation(self, idx_arr) :
        return idx_arr[0] != -1 and idx_arr[1] != -1 and idx_arr[2] != -1
    def smallestSubstring(self, s):
        n = len(s)
        last_seen = [-1] * 3
        min_dist = n + 1
        
        for i, ch in enumerate(s):
            last_seen[ord(ch) - ord('0')] = i
            
            if self.checkValidation(last_seen):
                min_dist = min(min_dist, i - min(last_seen[0], last_seen[1],last_seen[2]) + 1)
            
        return min_dist if min_dist != (n + 1) else -1


*****************


class Solution:
    
    def smallestSubstring(self, s):
        n = len(s)
        left = 0
        last_seen = [0] * 3
        min_dist = n + 1
        
        for right in range(n) :
            last_seen[ord(s[right]) - ord('0')] += 1
            while last_seen[0] and last_seen[1] and last_seen[2] :
                min_dist = min(min_dist, right - left + 1)
                last_seen[ord(s[left]) - ord('0')] -= 1
                left += 1
            
        return min_dist if min_dist != (n + 1) else -1
        
