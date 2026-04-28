# Longest Repeating Character Replacement


class Solution:
    def longestSubstr(self, s, k):
        freq = [0] * 26   # frequency array for A–Z
        left = 0
        maxFreq = 0
        ans = 0

        for right in range(len(s)):
            # update frequency of current character
            freq[ord(s[right]) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(s[right]) - ord('A')])

            # if more than k changes needed, shrink window
            while (right - left + 1) - maxFreq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            # update answer
            ans = max(ans, right - left + 1)

        return ans
