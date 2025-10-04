from copy import deepcopy
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        area = deepcopy(grid)
        count = 0
        def dfs(r, c, area):
            if(r<len(area)) and r>=0 and c>=0 and (c<len(area[0])) and area[r][c] == '1':
                area[r][c] = 'X'
                dfs(r+1,c,area)
                dfs(r-1,c,area)
                dfs(r,c+1,area)
                dfs(r,c-1,area)

            else: return


        for r in range(len(area)):
            for c in range(len(area[0])):
                value = area[r][c]
                if value == "1":
                    count += 1
                    dfs(r,c,area)
        return count
