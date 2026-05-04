#Palindrome Binary


class Solution:
    def isPallindrome(self, N):
        bits = []
        temp = N
        while temp :
            bits.append(temp & 1)
            temp >>= 1
        
        left = 0
        right = len(bits) - 1
        
        while left < right :
            if bits[left] != bits[right] :
                return 0
            left += 1
            right -= 1
        
        return 1
