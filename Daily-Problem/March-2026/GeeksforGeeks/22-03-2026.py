# Rotten Oranges


class Solution:
	def orangesRot(self, mat):
		if not mat:
            return -1

        n, m = len(mat), len(mat[0])
        queue = deque()
        fresh_oranges = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    queue.append((i, j, 0)) 
                elif mat[i][j] == 1:
                    fresh_oranges += 1

    
        paths = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time_to_rotten = 0

        while queue:
            i, j, time_to_rotten = queue.popleft()

            for pi, pj in paths:
                di, dj = i + pi, j + pj

                if 0 <= di < n and 0 <= dj < m and mat[di][dj] == 1:
                    mat[di][dj] = 2  
                    fresh_oranges -= 1
                    queue.append((di, dj, time_to_rotten + 1))

        return time_to_rotten if fresh_oranges == 0 else -1
