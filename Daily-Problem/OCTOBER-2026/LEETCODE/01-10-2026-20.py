# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stk = []
        mpp = ["(" , "{" , "["]

        for bracket in s :
            if bracket in mpp :
                stk.append(bracket)
            else :
                if not stk :
                    return False
                elif bracket == ")" and stk[-1] != "(":
                    return False
                elif bracket == "}" and stk[-1] != "{":
                    return False
                elif bracket == "]" and stk[-1] != "[":
                    return False

                stk.pop()

        return len(stk) == 0
