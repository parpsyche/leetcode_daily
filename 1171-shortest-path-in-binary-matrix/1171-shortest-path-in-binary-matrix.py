from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = 1
        
        q = deque([(0, 0, 1)])  # (x, y, distance)

        while q:
            x, y, d = q.popleft()
            if x == n-1 and y == n-1:
                return d
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and dist[nx][ny] > d + 1:
                    dist[nx][ny] = d + 1
                    q.append((nx, ny, d + 1))

        return -1