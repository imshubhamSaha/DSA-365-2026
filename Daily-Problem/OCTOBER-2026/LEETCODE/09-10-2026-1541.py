# 1541. Minimum Insertions to Balance a Parentheses String
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        opening = []

        answer = 0
        i = 0
        while i < n :
            bracket = s[i]
            if s[i] == '(' :
                opening.append(bracket)
                i += 1
            else :
                if i < (n - 1) :
                    if s[i+1] == ")" and opening:
                        opening.pop()
                        i += 2
                    elif s[i + 1] != ")" and opening:
                        opening.pop()
                        answer += 1
                        i += 1
                    elif not opening and s[i+1] != ")" :
                        answer += 2
                        i += 1
                    else :
                        answer += 1
                        i += 2
                else :
                    if opening :
                        answer += 1
                        opening.pop()
                    else :
                        answer += 2 
                    i += 1
            
        return answer + len(opening) * 2

                
