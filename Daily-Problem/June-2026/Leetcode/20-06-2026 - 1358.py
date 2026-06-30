# 1358. Number of Substrings Containing All Three Characters

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = [-1,-1,-1]
        valid_substr = 0

        for i in range(n) :
            cnt[ord(s[i]) - ord('a')] = i
            valid_substr += 1 + min(cnt)

        return valid_substr
