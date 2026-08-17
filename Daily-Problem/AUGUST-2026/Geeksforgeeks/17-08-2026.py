# Snake and Ladder Problem
from collections import deque
class Solution:
    def minThrows(self, n, lad, sn):
        N = n * n

        board = list(range(N + 1))
        
        for i in range(0, len(lad), 2):
            start = lad[i]
            end = lad[i + 1]
            board[start] = end


        for i in range(0, len(sn), 2):
            start = sn[i]
            end = sn[i + 1]
            board[start] = end


        q = deque([(1, 0)])
        visited = [False] * (N + 1)
        visited[1] = True

        while q:
            cell, throws = q.popleft()

            if cell == N:
                return throws

            for dice in range(1, 7):
                next_cell = cell + dice

                if next_cell > N:
                    continue

                next_cell = board[next_cell]

                if not visited[next_cell]:
                    visited[next_cell] = True
                    q.append((next_cell, throws + 1))

        return -1
        
