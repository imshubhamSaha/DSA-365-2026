#3121. Count the Number of Special Characters II

class Solution:
    def isCapital(self, char_code) :
        return char_code >= ord('A') and char_code <= ord('Z')

    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        special_letters = 0
        lower_case = [False] * 26
        upper_case = [False] * 26
        capital = ord('A')
        small = ord('a')
        for char in word :
            char_code = ord(char)
            idx = char_code - capital
            if self.isCapital(char_code) :
                upper_case[idx] = True
                continue
            idx = char_code - small
            lower_case[idx] = False if upper_case[idx] else True
            
        for i in range(26):
            if lower_case[i] and upper_case[i] :
                special_letters += 1    
        return special_letters

