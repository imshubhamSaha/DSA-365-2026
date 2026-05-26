# 3120. Count the Number of Special Characters I
class Solution:
    def checkCapital(self, char_code) :
        return char_code >= ord('A') and char_code <= ord('Z')

    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        count = [0] * 26
        
        special_letters = 0

        for ch in word :
            char_code = ord(ch)
            if self.checkCapital(char_code) :
                idx = char_code - ord('A')
                if count[idx] == 0 :
                    count[idx] = 2
                elif count[idx] == 1 :
                    count[idx] = 3
                    special_letters += 1
            else :
                idx = char_code - ord('a')
                if count[idx] == 0 :
                    count[idx] = 1
                elif count[idx] == 2 :
                    count[idx] = 3
                    special_letters += 1        
        return special_letters
