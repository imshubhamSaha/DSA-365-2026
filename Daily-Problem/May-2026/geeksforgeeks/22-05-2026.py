# 1s Surrounded by 0s

from collections import deque
class Solution:
    def cntOnes(self, grid):
        n = len(grid)
        m = len(grid[0])
        visited = set()
        
        def bfs(i, j):
            d = deque()
            d.append((i, j))
            visited.add((i, j))
            
            while d:
                x, y = d.popleft()
                
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        d.append((nx, ny))
        
        for j in range(m):
            if grid[0][j] == 1 and (0, j) not in visited:
                bfs(0, j)
        
        for j in range(m):
            if grid[n-1][j] == 1 and (n-1, j) not in visited:
                bfs(n-1, j)
        
        for i in range(n):
            if grid[i][0] == 1 and (i, 0) not in visited:
                bfs(i, 0)
        
        for i in range(n):
            if grid[i][m-1] == 1 and (i, m-1) not in visited:
                bfs(i, m-1)
        
        total_ones = sum(cell == 1 for row in grid for cell in row)
        
        return total_ones - len(visited)
