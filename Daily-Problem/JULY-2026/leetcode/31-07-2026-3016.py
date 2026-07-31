# 3016. Minimum Number of Pushes to Type Word II

class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8 :
            return n
        char_freq = [0] * 26

        for char in word :
            char_freq[ord(char) - ord('a')] += 1

        char_freq.sort()
        minimum_pushes = 0
        for i in range(25, -1,-1) :
            freq = char_freq[i]
            if freq == 0 :
                break
            minimum_pushes += ((25 - i) // 8 + 1) * freq

        return minimum_pushes
