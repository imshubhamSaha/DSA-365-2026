# 3014. Minimum Number of Pushes to Type Word I

class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        if n <= 8 :
            return n

        min_keys = 0

        for i in range(n) :
            min_keys += 1 + (i // 8)
        
        return min_keys
