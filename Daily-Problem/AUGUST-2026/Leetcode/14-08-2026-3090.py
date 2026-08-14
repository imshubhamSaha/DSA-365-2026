# 3090. Maximum Length Substring With Two Occurrences
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        freq = [0] * 26
        max_len = 0
        left = 0
        right = 0
        while right < n :
            char_idx = ord(s[right]) - ord('a')
            freq[char_idx] += 1

            while left < right and freq[char_idx] > 2 :
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
