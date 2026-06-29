# 1967. Number of Strings That Appear as Substrings in Word
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n = len(patterns)
        m = len(word)
        appeared = 0
        for i in range(n) :
            s = patterns[i]
            if s in word :
                appeared += 1
        
        return appeared
