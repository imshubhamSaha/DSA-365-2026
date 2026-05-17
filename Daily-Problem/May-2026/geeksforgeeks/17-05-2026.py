# Make the array beautiful

class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        beautiful_array = []
        
        for num in arr :
            if len(beautiful_array) :
                if (num >= 0 and beautiful_array[-1] < 0) or (num < 0 and beautiful_array[-1] >= 0) :
                    beautiful_array.pop()
                    continue
            beautiful_array.append(num)
        
        return beautiful_array
