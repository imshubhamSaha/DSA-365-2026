# 3498. Reverse Degree of a String
class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        product_sum = 0

        for i in range(n) :
            char_val = (26 - (ord(s[i]) - ord('a'))) 
            product_sum += char_val * (i + 1)
        
        return product_sum
