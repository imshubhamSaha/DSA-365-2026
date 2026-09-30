# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        answer = []
        depth = 0

        for paren in seq :
            if paren == "(" :
                answer.append(depth % 2)
                depth += 1
            else :
                depth -= 1
                answer.append(depth % 2)
        
        return answer
