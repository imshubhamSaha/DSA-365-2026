# Largest Zigzag Sequence
class Solution:
    def zigzagSequence(self, mat):
        n = len(mat)
        for i in range(1, n):
            # Find top two values and their indices in the previous row
            row = mat[i - 1]
            # Get index of max element
            first_i = max(range(n), key=row.__getitem__)
            first = row[first_i]
            # Get second largest by checking all except first_i
            second = max((row[j] for j in range(n) if j != first_i), default=0)

            # Update current row
            for j in range(n):
                mat[i][j] += first if j != first_i else second

        return max(mat[-1])
