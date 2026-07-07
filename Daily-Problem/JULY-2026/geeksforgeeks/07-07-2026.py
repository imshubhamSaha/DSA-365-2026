# Largest Unblocked Submatrix
class Solution:
    def largestArea(self, n, m, arr):
        # code here
        blocked_rows = [0, n+1]
        blocked_cols = [0, m+1]
        
        for r, c in arr:
            blocked_rows.append(r)
            blocked_cols.append(c)
            
        blocked_rows.sort()
        blocked_cols.sort()
        
        max_row_gap = max([blocked_rows[i]-blocked_rows[i-1]-1 for i in range(1, len(blocked_rows))], default = 0)
        max_col_gap = max([blocked_cols[j]-blocked_cols[j-1]-1 for j in range(1, len(blocked_cols))], default = 0)
        
        res = max_row_gap*max_col_gap
        return res
