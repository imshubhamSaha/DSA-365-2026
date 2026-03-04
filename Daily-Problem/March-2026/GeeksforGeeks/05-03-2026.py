# Longest Substring with K Uniques


class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        char_freq = [0] * 26
        distinct = 0
        left = 0
        longest_length = -1
        for right in range(n) :
            index = ord(s[right]) - ord('a')
            if char_freq[index] == 0 :
                distinct += 1
            char_freq[index] += 1
            while left < right  and distinct > k :
                idx = ord(s[left]) - ord('a')
                char_freq[idx] -= 1
                if char_freq[idx] == 0:
                    distinct -= 1
                left += 1
            if distinct == k :
                longest_length = max(longest_length, (right - left) + 1)
            
        return longest_length
        
