# Min Steps by Knight
from collections import deque
class Solution:
	def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
		#Code here
		if knightPos == targetPos:
             return 0

        direction = [[i, j]
            for i in (-2, -1, 1, 2)
                for j in (-2, -1, 1, 2)
                    if abs(i) + abs(j) == 3]

        q = deque()
        q.append([knightPos[0]-1, knightPos[1]-1, 0])

        visited = [[0]*n for i in range(n)]
        visited[knightPos[0]-1][knightPos[1]-1] = 1

        while q:
            x, y, steps = q.popleft()

            for x1, y1 in direction:
                x2, y2 = x+x1, y+y1

                if -1 < x2 < n and -1 < y2 < n and not visited[x2][y2]:
                    if x2 == targetPos[0]-1 and y2 == targetPos[1]-1:
                         return steps + 1
                    visited[x2][y2] = 1
                    q.append([x2, y2, steps+1])

        return -1
