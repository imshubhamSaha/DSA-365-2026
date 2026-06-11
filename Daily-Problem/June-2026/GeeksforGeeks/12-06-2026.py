# Equal Point in Brackets

class Solution:
    def findIndex(self, s):
        n = len(s)
        close_parenthesis = 0
        
        for pt in s :
            if pt == ')' :
                close_parenthesis += 1
        
        open_parenthesis = 0
        
        for i in range(n) :
            if open_parenthesis == close_parenthesis :
                return i 
            if s[i] == '(' :
                open_parenthesis += 1
            else :
                close_parenthesis -= 1
        return n
