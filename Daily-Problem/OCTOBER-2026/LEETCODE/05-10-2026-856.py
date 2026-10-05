#856. Score of Parentheses

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        score = [0]

        for b in s :
            if b == "(" :
                score.append(0)
            else :
                score.append(max(1, score.pop() * 2) + score.pop())

        return score.pop()
