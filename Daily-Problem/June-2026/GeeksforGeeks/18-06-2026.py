# Coverage of all Zeros in a Binary Matrix

class Solution:
    def findCoverage(self, mat):
        m = len(mat)
        n = len(mat[0])
        
        coverage = 0
        
        for i in range(m) :
            one_found = False
            total_zero = 0
            
            for j in range(n) :
                if mat[i][j] == 1 :
                    one_found = True
                    coverage += total_zero
                    total_zero = 0
                else :
                    coverage += int(one_found)
                    total_zero += 1

        for i in range(n) :
            one_found = False
            total_zero = 0
            
            for j in range(m) :
                if mat[j][i] == 1 :
                    one_found = True
                    coverage += total_zero
                    total_zero = 0
                else :
                    coverage += int(one_found)
                    total_zero += 1
                    
        return coverage
