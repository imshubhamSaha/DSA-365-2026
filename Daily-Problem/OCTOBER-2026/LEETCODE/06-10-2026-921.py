# 921. Minimum Add to Make Parentheses Valid
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        opening_bracket = 0

        make_valid = 0

        for bracket in s :
            if bracket == '(' :
                opening_bracket += 1
            else :
                if opening_bracket > 0 :
                    opening_bracket -= 1
                else :
                    make_valid += 1

        return make_valid + opening_bracket
