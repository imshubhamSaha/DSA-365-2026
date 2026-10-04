# 678. Valid Parenthesis String
class Solution:
    def checkValidString(self, s: str) -> bool:
        minParen = 0
        maxParen = 0

        for ch in s :
            if ch == '(' :
                minParen += 1
                maxParen += 1
            elif ch == ')' :
                maxParen -= 1
                minParen = max(minParen-1, 0)
            else :
                maxParen += 1
                minParen = max(minParen-1, 0)

            if maxParen < 0 :
                return False   

        return minParen == 0
