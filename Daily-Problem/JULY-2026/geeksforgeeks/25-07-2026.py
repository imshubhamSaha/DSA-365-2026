# Max Sum Square Sub-Matrix of Size k

class Solution:
    def maximumSum(self, mat, k):
        n = len(mat)
        for i in range(n) :
            for j in range(n) : 
                if (i-1) >= 0 :
                    mat[i][j] += mat[i-1][j]
                if (j-1) >= 0 :
                    mat[i][j] += mat[i][j-1]
                    
                if (i-1) >= 0 and (j-1) >= 0 :
                    mat[i][j] -= mat[i-1][j-1]
           
       
        max_sum = float('-inf')
       
        for i in range((n - k) + 1) :
            for j in range((n - k) + 1) :
                total_sum = 0
                if i== 0 and j == 0 :
                    total_sum = mat[i+k-1][j+k-1]
                elif i== 0 and j > 0 :
                    total_sum = mat[i+k-1][j+k-1] - mat[i+k-1][j-1]
                elif i > 0 and j == 0 :
                    total_sum = mat[i+k-1][j+k-1] - mat[i-1][j+k-1]
                else :
                   total_sum = mat[i+k-1][j+k-1] - mat[i-1][j+k-1]-mat[i+k-1][j-1] + mat[i-1][j-1]
               
                max_sum = max(max_sum, total_sum)
           
       
        return max_sum
