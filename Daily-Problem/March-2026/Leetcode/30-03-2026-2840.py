#2840. Check if Strings Can be Made Equal With Operations II

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        char_freq = [0] * 52


        for i in range(n) :
            offset = (i & 1) * 26
            c1 = ord(s1[i]) - ord("a")
            c2 = ord(s2[i]) - ord("a")
            char_freq[c1 + offset] += 1
            char_freq[c2 + offset] -= 1

        for i in range(52) :
            if char_freq[i] != 0 :
                return False
        
        return True
