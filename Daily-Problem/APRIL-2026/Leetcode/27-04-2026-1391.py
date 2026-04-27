#1391. Check if There is a Valid Path in a Grid

from collections import deque
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        dirs = {
            1: [(0, -1), (0, 1)],     
            2: [(-1, 0), (1, 0)],     
            3: [(0, -1), (1, 0)],     
            4: [(0, 1), (1, 0)],      
            5: [(0, -1), (-1, 0)],   
            6: [(0, 1), (-1, 0)]      
        }
        
        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }
        
        visited = [[False]*n for _ in range(m)]
        q = deque([(0, 0)])
        visited[0][0] = True
        
        while q:
            x, y = q.popleft()
            
            if (x, y) == (m - 1, n - 1):
                return True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if opposite[(dx, dy)] in dirs[grid[nx][ny]]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        
        return False
