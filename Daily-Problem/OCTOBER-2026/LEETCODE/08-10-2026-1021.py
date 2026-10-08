# 1021. Remove Outermost Parentheses
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        result = []
        valid = 0
        for i in range(n) :
            if s[i] == ")" :
                valid -= 1
            if valid > 0 :
                result.append(s[i])
            if s[i] == "(" :
                valid += 1

        return ''.join(result)
