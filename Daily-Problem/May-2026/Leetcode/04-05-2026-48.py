# 48. Rotate Image
class Solution:
    def reverse(self, matrix: List[List[int]]) -> None :
        n = len(matrix) 
        for i in range(n) :
            left = 0
            right = n - 1
            while left < right :
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1
            
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.reverse(matrix)
        for i in range(n-1, -1, -1) :
            for j in range(n-1, n-1-i, -1) :
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = temp
        

        
