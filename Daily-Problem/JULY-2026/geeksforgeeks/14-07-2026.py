# Smallest Non-Zero Number
class Solution:
    def find(self, arr):
        need = 0

        for val in reversed(arr):
            need = (need + val + 1) // 2   

        return need
        
