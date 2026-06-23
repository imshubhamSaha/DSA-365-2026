# Maximum Number of People Defeated

class Solution:
    def maxPeopleDefeated(self, p):
        strength = 1
        row = 1
        defeated = 0
        
        while strength <= p :
            p -= strength
            defeated += 1
            row += 1
            strength = row ** 2
            
        return defeated
        
