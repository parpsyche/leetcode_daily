from collections import deque
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        efforts[0][0] = 0
        
        q = deque([(0, 0, 0)])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while q:
            current_effort, r, c = q.popleft()
            
            if current_effort > efforts[r][c]:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    step_effort = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(current_effort, step_effort)
                    
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        q.append((new_effort, nr, nc))
                        
        result = efforts[rows-1][cols-1]
        return result if result != float('inf') else -1