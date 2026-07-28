# 3517. Smallest Palindromic Rearrangement I
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1 :
            return s
        char_freq = [0] * 26

        for char in s :
            idx = ord(char) - ord('a')
            char_freq[idx] += 1
        
        result = [''] * n
        left = 0
        right = n - 1
        char_idx = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        single_char = ''
        for i in range(26) :
            while char_freq[i] >= 2 and left < right:
                    result[left] = char_idx[i]
                    result[right] = char_idx[i]
                    char_freq[i] -= 2
                    left += 1
                    right -= 1
                
            if char_freq[i] == 1 :
                result[n // 2] = char_idx[i]
        
        print(result)
        return ''.join(result)        
